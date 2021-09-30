from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
dbURL = 'mysql+pymysql://root:admin@localhost/ecommerce'

app.config['SQLALCHEMY_DATABASE_URI'] = dbURL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
app.config['SECRET_KEY'] = 'GjIhOUzLBVs5CJ09j04KWg'

db = SQLAlchemy(app)
engine = create_engine(dbURL)
db.create_all()
db.session.commit()

from login import *
from model import *

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5000, threaded=True)