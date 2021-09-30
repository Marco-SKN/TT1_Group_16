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

/api/products [post]- 3
/api/products_orderitems [get] - 4
/api/orderitems [delete] - 5
/api/orders [put] - 6
/api/products [put] - 6
/api/orderitems [put] - 6
'''