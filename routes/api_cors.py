from flask import request, jsonify, Blueprint, send_file
from flask_pydantic_spec import Response
from modules.Invalidate import InvalidUsage
import datetime
import requests
from bson import ObjectId
from config.object_str import CutId
from modules.swagger import api
from config.db import MongoDB
from features_line.flex_message import flex_notify_channel, flex_notify_channel_subject
from routes.wh_notify import line_bot_api_notify
from environ.client_environ import MONGODB_URI
from machine_leanning.model_spam import model_spam
import os
import json

public = Blueprint('public', __name__, template_folder='templates')

# client = 'mongodb://127.0.0.1:27017'
# client = os.environ.get('MONGODB_URI')
db = MongoDB(database_name='Mango', uri=MONGODB_URI)
collection = 'imports'


@public.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def split_text_coma(text: str):
    sentence = text.split(',')
    return sentence[1]


def condition_message(channel, date, time, company, name, tel, email, product,
                      message, subject=None):
    users = db.find(collection='line_follower_notify', query={'approval_status': True})
    users = list(users)
    for user in users:
        if subject:
            if subject in user['model_subject']:
                line_bot_api_notify.push_message(user['user_id'],
                                                 flex_notify_channel_subject(channel=channel,
                                                                             date_time=f'{date} {time}',
                                                                             company=company,
                                                                             name=name, tel=tel,
                                                                             email=email, product=product,
                                                                             message=message, subject=subject))
        elif channel != 'Contact':
            if product in user['model']:
                line_bot_api_notify.push_message(user['user_id'],
                                                 flex_notify_channel(channel=channel,
                                                                     date_time=f'{date} {time}',
                                                                     company=company,
                                                                     name=name, tel=tel,
                                                                     email=email, product=product,
                                                                     message=message))


def key_model_transaction(item: dict, channel: str, userId=None, email_private=None, profile=None, picture=None,
                          other=None) -> dict:
    item['other'] = other
    item['userId'] = userId
    item['email_private'] = email_private
    item['profile'] = profile
    item['picture'] = picture
    item['channel'] = channel
    item['username'] = None
    item['uid'] = None
    item['tag'] = []
    if item['product'] == 'Mango ERP (Construction)': item['product'] = 'Construction'
    if item['product'] == 'Mango ERP (Real Estate)': item['product'] = 'RealEstate'
    if item['product'] == 'Pusit (Consulting)': item['product'] = 'Consulting'
    if item['company'] == 'google': item['tag'] = ['spam']
    if item['message']:
        predict = item['tag'] = model_spam(item['message'])
        if predict == ['not spam']:
            item['tag'] = []
    return item


@public.route('/api/demorequest', methods=['POST'])
@api.validate(resp=Response(HTTP_200=None, HTTP_400=None), tags=['customer'])
def get_demo():
    try:
        item = request.get_json()
        key = CutId(_id=ObjectId()).dict()['id']
        _d = datetime.datetime.now()
        item['name'] = item.pop('fname')
        item["date"] = _d.strftime("%d/%m/%y")
        item["time"] = _d.strftime("%H:%M:%S")
        item["id"] = key
        item = key_model_transaction(item, 'GetDemo')
        db.insert_one(collection=collection, data=item)

        name = item['name']
        product = item['product']
        tel = item['tel']
        channel = item['channel']
        date = item['date']
        time = item['time']
        email = item['email']
        message = item['message']
        company = item['company']
        tag = item['tag']
        del item['_id']
        if company == 'google' or tag == ['spam']:
            return jsonify(item)
        else:
            condition_message(channel, date, time, company, name, tel, email, product, message)
        return jsonify(item)
    except:
        raise InvalidUsage(message='please try again', status_code=400, payload={'status': True})


@public.route('/api/contract', methods=['POST'])
@api.validate(resp=Response(HTTP_200=None, HTTP_400=None), tags=['customer'])
def contact():
    try:
        item = request.get_json()
        key = CutId(_id=ObjectId()).dict()['id']
        _d = datetime.datetime.now()
        item['email'] = item.pop('contact_email')
        item['name'] = item.pop('contact_name')
        item['company'] = item.pop('contact_name_company')
        item['product'] = item.pop('contact_subject')
        item['tel'] = item.pop('contact_tel')
        item['message'] = item.pop('contact_message')
        item["date"] = _d.strftime("%d/%m/%y")
        item["time"] = _d.strftime("%H:%M:%S")
        item["id"] = key
        sentence = split_text_coma(item.get('contact_email_div'))
        item['subject'] = sentence
        item = key_model_transaction(item, 'Contact')
        db.insert_one(collection=collection, data=item)

        name = item['name']
        product = item['product']
        tel = item['tel']
        channel = item['channel']
        date = item['date']
        time = item['time']
        email = item['email']
        message = item['message']
        company = item['company']
        tag = item['tag']
        del item['_id']
        if company == 'google' or tag == ['spam']:
            return jsonify(item)
        else:
            condition_message(channel, date, time, company, name, tel, email, product, message, sentence)
        return jsonify(item)
    except:
        raise InvalidUsage(message='please try again', status_code=400, payload={'status': True})


@public.route('/api/preview/excel', methods=['GET'])
@api.validate(resp=Response(HTTP_200=None, HTTP_400=None), tags=['customer'])
def preview_excel():
    file = os.path.join('static', 'excels/preview.xlsx')
    return send_file(file, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                     attachment_filename='preview.xlsx')


@public.route('/requests/token/checkToken')
def request_token():
    param = request.args.get('token')
    collect = request.args.get('collection')
    print(collect)
    if collect:
        url = 'https://marketing.mangoanywhere.com/estate/api/public/CheckToken'
        headers = {
            'x-mg-api-token': param
        }
        response = requests.request("GET", url, headers=headers)
        res = response.json()
        return jsonify(res)
    url = "https://poc.mangoanywhere.com/test_websql/api/public/CheckToken"
    headers = {
        'x-mg-api-token': param
    }
    response = requests.request("GET", url, headers=headers)
    res = response.json()
    return jsonify(res)


@public.route('/requests/dynamic/optional', methods=['POST'])
def request_validation():
    item = request.get_json()
    param = item['token']
    url = item['url']
    data = item['data']
    headers = {
        'x-mg-api-token': param
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    res = response.json()
    return jsonify(res)


@public.route('/requests/token/account')
def account_token():
    collect = request.args.get('collection')
    if collect != 'customers':
        user = {
            "company": "MG1",
            "userid": "api01",
            "userpass": "1"
        }
        path = 'https://poc.mangoanywhere.com/test_websql/api/public/RequestApiToken'
        res = requests.post(url=path, json=user)
        res = res.json()
        return jsonify(user={}, token=res['data']['token'], status=False)
    else:
        res = {
            "company": "MG1",
            "userid": "API01",
            "userpass": "1234"
        }
        path = 'https://marketing.mangoanywhere.com/estate/api/public/RequestApiToken'
        res = requests.post(url=path, json=res)
        res = res.json()
        return jsonify(user={}, token=res['data']['token'], status=False)
