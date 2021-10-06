from flask import request, jsonify, Blueprint, send_file
from flask_pydantic_spec import Response
from modules.Invalidate import InvalidUsage
import datetime
from bson import ObjectId
from config.object_str import CutId
from modules.swagger import api
from config.db import MongoDB
from features_line.flex_message import flex_notify_channel
from routes.wh_notify import line_bot_api_notify
from environ.client_environ import MONGODB_URI
from machine_leanning.model_spam import model_spam
import os

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


def condition_message(channel, date, time, company, name, tel, email, product,
                      message):
    if message:
        users = db.find(collection='line_follower_notify', query={})
        users = list(users)
        for user in users:
            if user['approval_status']:
                if product in user['model']:
                    line_bot_api_notify.push_message(user['user_id'],
                                                     flex_notify_channel(channel=channel, date_time=f'{date} {time}',
                                                                         company=company,
                                                                         name=name, tel=tel,
                                                                         email=email, product=product, message=message))
    else:
        users = db.find(collection='line_follower_notify', query={})
        users = list(users)
        for user in users:
            if user['approval_status']:
                if product in user['model']:
                    line_bot_api_notify.push_message(user['user_id'],
                                                     flex_notify_channel(channel=channel, date_time=f'{date} {time}',
                                                                         company=company,
                                                                         name=name, tel=tel,
                                                                         email=email, product=product,
                                                                         message='ไม่มีข้อความ'))


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
        del item['contact_email_div']
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
            condition_message(channel, date, time, company, name, tel, email, product, message)
        return jsonify(item)
    except:
        raise InvalidUsage(message='please try again', status_code=400, payload={'status': True})


@public.route('/api/preview/excel', methods=['GET'])
@api.validate(resp=Response(HTTP_200=None, HTTP_400=None), tags=['customer'])
def preview_excel():
    file = os.path.join('static', 'excels/preview.xlsx')
    return send_file(file, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                     attachment_filename='preview.xlsx')


@public.route('/requests/token/account')
def account_token():
    collect = request.args.get('collection')
    if collect != 'customers':
        res = {
            "company": "MG1",
            "userid": "api01",
            "userpass": "1"
        }
        return jsonify(res)
    else:
        res = {
            "company": "MG1",
            "userid": "api01",
            "userpass": "1234"
        }
        return jsonify(res)
