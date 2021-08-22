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
collection = 'tags_customer'


@route_tag.route('/api/tag')
@api.validate(tags=['Tag'])
def find_tag():
    tag = request.args.get('tag')
    if tag:
        key = CutId(_id=ObjectId()).dict()['id']
        data = {'text': tag, 'id': key}
        db.insert_one(collection='tags_customer', data=data)
        return {'message': 'success'}
    data = db.find(collection=collection, query={})
    data = list(data)
    for v in data:
        del v['_id']
    return jsonify(data[::-1])


@route_tag.route('/api/tag/<string:item>', methods=['POST'])
@api.validate(tags=['Tag'])
def add_tag(item):
    id = request.args.get('id-query')
    query = {'id': id}
    values = {'$set': {'text': item}}
    db.update_one(collection=collection, query=query, values=values)
    return jsonify({'item': item, 'q': id})


@route_tag.route('/api/tag', methods=['DELETE'])
@api.validate(tags=['Tag'])
def delete_tag():
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
    print(item)
    if item.get('href') == 'import':
        query_collection_tag(item, 'imports')
    elif item.get('href') == 'customer':
        query_collection_tag(item, 'customers')
    return jsonify(item)
