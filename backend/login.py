from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Date, func
from datetime import datetime, timedelta
import jwt

app = Flask(__name__)
dbURL = 'mysql://root@localhost/ecommerce'
app.config['SQLALCHEMY_DATABASE_URI'] = dbURL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)
app.config['SECRET_KEY'] = 'GjIhOUzLBVs5CJ09j04KWg'


class Customer(db.Model):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    created_at = Column(Date, server_default=func.now())


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
        user = Customer.query.filter_by(username=decoded['sub']).first()
        if user:
            return True
    except:
        return False
    return False


@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    username = payload['username']
    password = payload['password']
    user = Customer.query.filter_by(
        username=username, password=password).first()
    if user:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': username
        }
        return jwt.encode(payload, app.config.get('SECRET_KEY'), algorithm='HS256')
    else:
        return "Unauthorised", 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
