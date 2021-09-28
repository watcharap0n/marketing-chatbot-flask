from flask import request, jsonify, Blueprint
from flask_pydantic_spec import Response
from modules.Invalidate import InvalidUsage
import datetime
from bson import ObjectId
from config.object_str import CutId
from modules.swagger import api
from config.db import MongoDB
from environ.client_environ import MONGODB_URI
from routes.api_cors import key_model_transaction, condition_message
import os

question = Blueprint('question', __name__, template_folder='templates')

# client = 'mongodb://127.0.0.1:27017'
# client = os.environ.get('MONGODB_URI')
db = MongoDB(database_name='Mango', uri=MONGODB_URI)
collection = 'imports'


@question.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@question.route('/api/all/questionnaire', methods=['POST'])
@api.validate(resp=Response(HTTP_201=None, HTTP_400=None), tags=['Questionnaire'])
def api_send_all_question():
    query_collection = request.args.get('collection')
    item = request.get_json()
    key = CutId(_id=ObjectId()).dict()['id']
    _d = datetime.datetime.now()
    item["date"] = _d.strftime("%d/%m/%y")
    item["time"] = _d.strftime("%H:%M:%S")
    item["id"] = key
    channel = item.get('channel')
    userId = item.get('userId')
    email_private = item.get('email_private')
    profile = item.get('profile')
    picture = item.get('picture')
    other = item.get('other')
    item = key_model_transaction(item=item, channel=channel, userId=userId, email_private=email_private,
                                 profile=profile,
                                 picture=picture, other=other)
    db.insert_one(query_collection, item) if query_collection else db.insert_one(collection, item)
    name = item['name']
    product = item['product']
    tel = item['tel']
    channel = item['channel']
    date = item['date']
    time = item['time']
    email = item['email']
    message = item['message']
    company = item['company']
    del item['_id']
    condition_message(channel, date, time, company, name, tel, email, product, message)
    res = {'message': 'success'}
    return jsonify(res)


@question.route('/api/form/custom/object')
@api.validate(resp=Response(HTTP_201=None, HTTP_400=None), tags=['Questionnaire'])
def get_custom_form_object():
    query = {'collection': request.args.get('collection')}
    items = db.find(collection='form_custom', query=query)
    items = list(items)
    for id in items:
        del id['_id']
    return jsonify(items)


@question.route('/api/form/custom/get', methods=['GET'])
@api.validate(resp=Response(HTTP_201=None, HTTP_400=None), tags=['Questionnaire'])
def get_custom_form_line():
    id = request.args.get('id')
    item = db.find_one(collection='form_custom', query={'id': id})
    del item['_id']
    return jsonify(message=id, item=item)


@question.route('/api/form/custom/add/form', methods=['POST'])
@api.validate(resp=Response(HTTP_201=None, HTTP_400=None), tags=['Questionnaire'])
def post_custom_form():
    data = request.get_json()
    key = CutId(_id=ObjectId()).dict()['id']
    _d = datetime.datetime.now()
    data["date"] = _d.strftime("%d/%m/%y")
    data["time"] = _d.strftime("%H:%M:%S")
    data["id"] = key
    data['href'] = f'https://mangoconsultant.net/custom/page/{key}'
    db.insert_one(collection='form_custom', data=data)
    del data['_id']
    return jsonify(data)


@question.route('/api/form/custom/delete/form/<string:id>', methods=['DELETE'])
@api.validate(resp=Response(HTTP_201=None, HTTP_400=None), tags=['Questionnaire'])
def delete_custom_form(id):
    query = {'id': id}
    db.delete_one(collection='form_custom', query=query)
    res = {'message': 'success'}
    return jsonify(res)


@question.route('/api/form/custom/update/product/<string:id>', methods=['PUT'])
@api.validate(resp=Response(HTTP_201=None, HTTP_400=None), tags=['Questionnaire'])
def update_custom_form_line(id):
    data = request.get_json()
    query = {'id': id}
    values = {'$set': data}
    item = db.update_one(collection='form_custom', query=query, values=values)
    print(item)
    res = {'message': 'success'}
    return jsonify(res)


@question.route('/api/form/custom/delete/product/<string:id>', methods=['DELETE'])
@api.validate(resp=Response(HTTP_201=None, HTTP_400=None), tags=['Questionnaire'])
def delete_custom_form_line(id):
    query = {'id': id}
    db.delete_one(collection='form_custom', query=query)
    res = {'message': 'success'}
    return jsonify(res)
