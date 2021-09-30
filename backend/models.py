from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    postal_code = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    created_at = db.Column(db.Date, server_default=db.func.now())

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey(
        'customer.id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.current_timestamp())

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class Order_item(db.Model):
    __tablename__ = 'order_item'
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(
        'order.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    product_qty = db.Column(db.Integer, server_default=None)
    total_price = db.Column(db.Float, server_default=None)

    def json(self):
        return {"product_id": self.product_id, "product_qty": self.product_qty, "total_price": self.total_price}

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    image = db.Column(db.Integer, nullable=False)
    qty = db.Column(db.Integer, nullable=False)

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}