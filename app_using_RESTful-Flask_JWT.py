from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserResgister
from resources.item import Item, Items
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'vick'
api = Api(app)


jwt = JWT(app, authenticate, identity)  # jwt creates new endpoint i.e. /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserResgister, '/register')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000)
