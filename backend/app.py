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


@app.route('/cart/retrieve', methods=['GET'])
def get_orderitems():
    orderid = get_orderid(g.user.id)
    return jsonify({"order_items": [orderitem.json() for orderitem in Order_item.query.filter_by(order_id=orderid).all()]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
