from flask import request, jsonify, Blueprint
from flask_pydantic_spec import Response
from config.db import MongoDB
from bson import ObjectId
from modules.swagger import api
from config.object_str import CutId
from environ.line_token import mango_channel
from environ.client_environ import MONGODB_URI
import os

route_intent = Blueprint('intents', __name__, template_folder='templates')

# client = 'mongodb://127.0.0.1:27017'
# client = os.environ.get('MONGODB_URI')
db = MongoDB(database_name='Mango', uri=MONGODB_URI)
collection = 'intents'


@route_intent.route('/intent/data', methods=['POST'])
@api.validate(tags=['Intent'])
def data_intent():
    access_token = request.get_json()
    if access_token:
        access_token = access_token.get('access_token')
        data = db.find(collection=collection, query={'access_token': access_token})
        data = list(data)
        return jsonify(data)
    data = db.find(collection=collection, query={'access_token': mango_channel})
    data = list(data)
    return jsonify(data)


@route_intent.route('/intent/add', methods=['POST'])
@api.validate(resp=Response(HTTP_201=None, HTTP_403=None), tags=['Intent'])
def add_intent():
    item = request.get_json()
    key = CutId(_id=ObjectId()).dict()['id']
    if item.get('access_token'):
        item['id'] = key
        db.insert_one(collection=collection, data=item)
        del item['_id']
        return jsonify(item)
    item['access_token'] = mango_channel
    item['id'] = key
    db.insert_one(collection=collection, data=item)
    del item['_id']
    return jsonify(item)


@route_intent.route('/intent/query/<string:id>', methods=['PUT'])
@api.validate(tags=['Intent'])
def query_intent(id):
    data = db.find_one(collection=collection, query={'id': id})
    data = dict(data)
    res = {'message': data}
    return jsonify(res)


@route_intent.route('/intent/update_intent/<string:id>', methods=['PUT'])
@api.validate(tags=['Intent'])
def update_intent(id):
    data = request.get_json()
    query = {'id': id}
    values = {'$set': data}
    db.update_one(collection=collection, query=query, values=values)
    res = {'message': 'success'}
    return jsonify(res)


@route_intent.route('/intent/delete_intent/<string:id>', methods=['DELETE'])
@api.validate(tags=['Intent'])
def delete_intent(id):
    db.delete_one(collection=collection, query={'id': id})
    res = {'message': 'success'}
    return jsonify(res)
