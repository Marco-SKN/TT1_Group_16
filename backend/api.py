from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from model import *
from app import db

class myApi(Resource):
    def get(self, id=None):
        return {'test':'get'}

    def post(self, id=None):        
        return {'test':'post'}

    def put(self, id=None):        
        return {'test':'put'}

    def delete(self, id=None)
        return {'test':'delete'}

'''
You must have an API to return a list of all products from Products and 
Category table [2]
• You must set up the respective shopping cart API with the following 
functionalities:
− Insert products added from frontend cart into database [3]
− Return a list of all products from the OrderItem table [4]
− Delete from the OrderItem table [5]
− Update the Orders, Products, and OrderItem table [6]
'''

'''
/api/products [get]- 2
/api/categories [get]- 2
/api/products_orderitems [get] - 4

/api/products [post]- 3
/api/orderitems [delete] - 5
/api/orders [put] - 6
/api/products [put] - 6
/api/orderitems [put] - 6
'''
def lst_products():
    products = Product.query.all()
    return [p.as_dict() for p in products]
def lst_categories():
    categories = Category.query.all()
    return [c.as_dict() for c in categories]
def lst_product_orderitems():
    pass

def add_product(json):
    p = Product(**json)
    db.session.add()

    if (not Product.query.get(json['id'])):
        db.session.add(item)
        db.session.commit()
    else:
        return {'message':'item already exist'}

def del_orderitem():
    pass

def update_order(json):
    if (Order.query.get(id)):
        Order.query.filter_by(id=id).update(json)
        db.session.commit()
        return json
    else:
        return {'message': 'item not found'}

def update_product(json):
    if (Product.query.get(id)):
        Product.query.filter_by(id=id).update(json)
        db.session.commit()
        return json
    else:
        return {'message': 'item not found'}

def update_orderitem(json):
    if (Order_item.query.get(id)):
        Order_item.query.filter_by(id=id).update(json)
        db.session.commit()
        return json
    else:
        return {'message': 'item not found'}

