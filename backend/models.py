from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    postal_code = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    created_at = db.Column(db.Date, server_default=db.func.now())


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # auto incrreament
    customer_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.current_timestamp(),
                           server_onupdate=db.func.current_timestamp())
    customer = db.Column(db.Integer, db.ForeignKey('customer.id'))
    # CONSTRAINT `customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE


class Order_item(db.Model):  # notdone
    product_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, primary_key=True)
    product_qty = db.Column(db.Integer, server_default=None)
    total_price = db.Column(db.Float, server_default=None)
    #  CONSTRAINT `order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    # CONSTRAINT `product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    image = db.Column(db.Integer, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    # CONSTRAINT `category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
