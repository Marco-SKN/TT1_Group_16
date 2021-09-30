from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from model import *
from app import db

class myApi(Resource):
    def get(self, id=None):
        # if id is None:
        #     items = Item.query.all()
        #     return {a.id:a.data for a in items}

        # item = Item.query.get(id)
        # return {id: item.data}

        return {'test':'get'}

    def post(self, id=None):
        # if not id:
        #     id = request.json['id']
        # data = request.json['data']
        # item = Item(id = id, data = data)

        # if (Item.query.get(id)):
        #     db.session.add(item)
        #     db.session.commit()
        # return {id: data}
        
        return {'test':'post'}

    def put(self, id=None):
        # if not id:
        #     id = request.json['id']
        # data = request.json['data']
        # if (Item.query.get(id)):
        #     Item.query.filter_by(id=id).update({'data': data})
        #     db.session.commit()
        #     return {id: data}
        # else:
        #     return {'message': 'item not found'}

        
        return {'test':'put'}
