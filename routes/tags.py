from flask import request, jsonify, Blueprint
from config.db import MongoDB
from config.object_str import CutId
from bson import ObjectId
from modules.swagger import api
from environ.client_environ import MONGODB_URI
import os

route_tag = Blueprint('tags', __name__, template_folder='templates')

# client = 'mongodb://127.0.0.1:27017'
# client = os.environ.get('MONGODB_URI')
db = MongoDB(database_name='Mango', uri=MONGODB_URI)


@route_tag.route('/api/tag')
@api.validate(tags=['Tag'])
def find_tag():
    collection = request.args.get('collection')
    data = db.find(collection=collection, query={})
    data = list(data)
    return jsonify(data[::-1])


@route_tag.route('/api/tag/add/new')
@api.validate(tags=['Tag'])
def add_tag():
    tag = request.args.get('tag')
    collection = request.args.get('collection')
    print(tag)
    print(collection)
    key = CutId(_id=ObjectId()).dict()['id']
    data = {'text': tag, 'id': key}
    db.insert_one(collection=collection, data=data)
    return {'message': 'success'}


@route_tag.route('/api/tag/<string:id>', methods=['PUT'])
@api.validate(tags=['Tag'])
def update_tag(id):
    collection = request.args.get('collection')
    item = request.get_json()
    print(id, 'id')
    print(collection, 'collection')
    print(item)
    query = {'id': id}
    values = {'$set': {'text': item['text']}}
    db.update_one(collection=collection, query=query, values=values)
    return jsonify({'item': item, 'q': id})


@route_tag.route('/api/tag', methods=['DELETE'])
@api.validate(tags=['Tag'])
def delete_tag():
    collection = request.args.get('collection')
    id = request.args.get('id-query')
    db.delete_one(collection=collection, query={'id': id})
    res = {'message': 'success'}
    return jsonify(res)


def query_collection_tag(item: dict, collect: str):
    id = item['id']
    value = [x['text'] for x in item['tag']]
    for i in id:
        db.update_one(collection=collect, query={'id': i['id']}, values={'$set': {'tag': value}})


@route_tag.route('/api/tag', methods=['POST'])
@api.validate(tags=['Tag'])
def post_tag():
    item = request.get_json()
    if item.get('href') == 'import':
        query_collection_tag(item, item['_import'])
    elif item.get('href') == 'customer':
        query_collection_tag(item, item['collection'])
    return jsonify(item)
