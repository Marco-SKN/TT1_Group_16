from models import *
from flask import Flask, request, g,  jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import jwt

app = Flask(__name__)
dbURL = 'mysql://root@localhost/ecommerce'
app.config['SQLALCHEMY_DATABASE_URI'] = dbURL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)
app.config['SECRET_KEY'] = 'GjIhOUzLBVs5CJ09j04KWg'

engine = create_engine(dbURL)
db.create_all()
db.session.commit()


@app.before_request
def before_request():
    if request.endpoint != 'login':
        token = request.headers.get('Authorization')
        if token:
            token = token.split()[1]
        if not checkjwt(token):
            return "Unauthorised", 403


def checkjwt(token):
    try:
        decoded = jwt.decode(token, app.config.get('SECRET_KEY'), options={
                             "require": ["exp", "iat", "sub"]}, algorithms=["HS256"])
        id = decoded['sub']
        g.user = Customer.query.filter_by(id=id).first()
        return g.user
    except:
        return None


@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    username = payload['username']
    password = payload['password']
    customer = Customer.query.filter_by(
        username=username, password=password).first()
    if customer:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': customer.id
        }
        return jwt.encode(payload, app.config.get('SECRET_KEY'), algorithm='HS256')
    else:
        return "Unauthorised", 403


def get_orderid(userid):
    existing_cart = Order.query.filter_by(
        customer_id=userid, status=0).first()
    if existing_cart:
        return existing_cart.id
    else:
        data = {"customer_id": userid, "status": 0}
        new_cart = Order(**data)
        db.session.add(new_cart)
        db.session.commit()
        return new_cart.id

@app.route('/api/products')
def lst_products():
    products = Product.query.all()
    return jsonify([p.as_dict() for p in products])

@app.route('/api/categories')
def lst_categories():
    categories = Category.query.all()
    return jsonify([c.as_dict() for c in categories])

@app.route('/cart/retrieve', methods=['GET'])
def get_orderitems():
    order_id = get_orderid(g.user.id)
    return jsonify({"order_items": [orderitem.json() for orderitem in Order_item.query.filter_by(order_id=order_id).all()]})

@app.route('/cart/insert', methods=['POST'])
def insert_orderitems():
    order_id = get_orderid(g.user.id)
    payload = request.get_json()
    product_id = payload['product_id']
    product_qty = int(payload['product_qty'])
    existing_item = Order_item.query.filter_by(
        order_id=order_id, product_id=product_id).first()
    if existing_item:
        product_qty += existing_item.product_qty
    price = float(Product.query.filter_by(id=product_id).first().price)
    data = {"product_id": product_id, "order_id": order_id,
            "product_qty": product_qty, "total_price": product_qty*price}
    db.session.merge(Order_item(**data))
    db.session.commit()
    return "Inserted", 200


@app.route('/cart/delete', methods=['POST'])
def delete_orderitems():
    order_id = get_orderid(g.user.id)
    payload = request.get_json()
    product_id = payload['product_id']
    existing_item = Order_item.query.filter_by(
        order_id=order_id, product_id=product_id).first()
    db.session.delete(existing_item)
    db.session.commit()
    return "Deleted", 200


@app.route('/cart/checkout', methods=['GET'])
def checkout():
    order_id = get_orderid(g.user.id)
    order_items = Order_item.query.filter_by(order_id=order_id).all()
    for item in order_items:
        product_id = item.product_id
        product_qty = int(item.product_qty)
        inventory_product = Product.query.filter_by(id=product_id).first()
        new_qty = int(inventory_product.qty) - product_qty
        inventory_product.qty = new_qty
        db.session.delete(item)
    order = Order.query.filter_by(order_id=order_id).first()
    order.status = 1
    db.session.commit()
    return "Checked out", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
