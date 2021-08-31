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


@question.route('/api/line/questionnaire', methods=['POST'])
@api.validate(resp=Response(HTTP_201=None, HTTP_400=None), tags=['Questionnaire'])
def q_line():
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
    db.insert_one(collection, item)
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


@question.route('/api/facebook/questionnaire', methods=['POST'])
@api.validate(resp=Response(HTTP_201=None, HTTP_400=None), tags=['Questionnaire'])
def q_facebook():
    try:
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
        item = key_model_transaction(item=item, channel=channel, userId=userId, email_private=email_private, profile=profile,
                                     picture=picture, other=other)
        db.insert_one(collection=collection, data=item)
        del item['_id']
        return item
    except:
        raise InvalidUsage(status_code=400, message='api something wrong!')
