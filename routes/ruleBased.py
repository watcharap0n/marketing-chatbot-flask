from flask import Blueprint, request, jsonify
from config.object_str import CutId
from bson import ObjectId
from config.db import MongoDB
from environ.line_token import mango_channel
from environ.client_environ import MONGODB_URI
import os

# client = 'mongodb://127.0.0.1:27017'
# client = os.environ.get('MONGODB_URI')
db = MongoDB(database_name='Mango', uri=MONGODB_URI)
collection = 'match_rule_based'
rule_base = Blueprint('rule_based', __name__, template_folder='templates')


@rule_base.route('/callback/mango/get_rule_based', methods=['POST'])
def get_rule_based():
    access_token = request.get_json()
    if access_token:
        access_token = access_token.get('access_token')
        data = db.find(collection=collection, query={'access_token': access_token})
        data = list(data)
        for v in data:
            del v['_id']
        return jsonify(data)
    data = db.find(collection=collection, query={'access_token': mango_channel})
    data = list(data)
    for v in data:
        del v['_id']
    return jsonify(data)


@rule_base.route('/callback/mango/match_rule_based', methods=['POST'])
def match_rule_based():
    """
    - Create Keyword RuleBased
    :return:
    """
    item = request.get_json(force=True)
    key = CutId(_id=ObjectId()).dict()['id']
    item['access_token'] = mango_channel
    item['id'] = key
    db.insert_one(collection, item)
    del item['_id']
    return jsonify(item)


@rule_base.route('/callback/mango/update_rule_based', methods=['POST'])
def update_rule_based():
    """
    - Update Keyword RuleBased
    :return:
    """
    item = request.get_json(force=True)
    # check = db.find_one(collection=collection, query={'keyword': item['keyword']})
    # if not check:
    id = item['id']
    query = {'id': id}
    values = {'$set': item}
    db.update_one(collection=collection, query=query, values=values)
    res = {'message': 'success', 'status': True}
    return jsonify(res)


# res = {'message': 'failed', 'status': False}
# return jsonify(res)


@rule_base.route('/callback/mango/delete_rule_based/<string:id>', methods=['DELETE'])
def delete_intent(id):
    db.delete_one(collection=collection, query={'id': id})
    res = {'message': 'success'}
    return jsonify(res)
