
from .app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Date, func

dbURL = 'mysql://root@localhost/ecommerce'

db = SQLAlchemy(app)
engine = create_engine(dbURL)
db.create_all()
db.session.commit()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    postal_code = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.Date, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True) # auto incrreament
    customer_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, 
            server_default=db.func.current_timestamp(), 
            server_onupdate=db.func.current_timestamp())
    customer = db.Column(db.Integer, db.ForeignKey('customer.id'))
    #CONSTRAINT `customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE


class Order_item(db.Model): #notdone
    product_id = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, server_default=None)
    product_qty = db.Column(db.Integer, server_default=None)
    total_price = db.Column(db.Float, server_default=None)
    #  CONSTRAINT `order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    # CONSTRAINT `product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE


class Product(db.Model):
    id = db.column(db.Integer, nullable=False)
    title = db.column(db.Integer, nullable=False)
    price = db.column(db.Float, nullable=False)
    description = db.column(db.Integer, nullable=False)
    category_id = db.column(db.Integer, nullable=False)
    image = db.column(db.Integer, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    # CONSTRAINT `category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE