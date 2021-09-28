from flask import request, jsonify, Blueprint
from flask_pydantic_spec import Response
from modules.swagger import api
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import StickerSendMessage, TextSendMessage, FlexSendMessage
from machine_leanning.model_text_classifire import intent_model
from environ.client_environ import MONGODB_URI
from random import randint
from bson import ObjectId
from config.object_str import CutId
from config.db import MongoDB
from numpy import random
import uuid
import json
from features_line import card, flex_message
import os

# client = 'mongodb://127.0.0.1:27017'
# client = os.environ.get('MONGODB_URI')
db = MongoDB(database_name='Mango', uri=MONGODB_URI)
collection = 'line_bot'

route_callback = Blueprint('callback', __name__, template_folder='templates')


@route_callback.route('/callback/save', methods=['POST'])
@api.validate(resp=Response(HTTP_201=None, HTTP_403=None), tags=['Callback'])
def save():
    result = request.get_json()
    key = CutId(_id=ObjectId()).dict()['id']
    path_wh = uuid.uuid4().hex
    result['id'] = key
    result['token'] = path_wh
    result['webhook'] = f'https://mangoconsultant.net/callback/{path_wh}'
    db.insert_one(collection=collection, data=result)
    del result['_id']
    return jsonify(result)


def get_profile(user_id, q):
    line_bot_api = q['ACCESS_TOKEN']
    line_bot_api = LineBotApi(line_bot_api)
    profile = line_bot_api.get_profile(user_id)
    displayName = profile.display_name
    userId = profile.user_id
    img = profile.picture_url
    status = profile.status_message
    result = {'displayName': displayName, 'userId': userId, 'img': img, 'status': status}
    return result


@route_callback.route('/callback/<string:token>', methods=['POST'])
@api.validate(tags=['Callback'])
def webhook(token):
    raw_json = request.get_json()
    q = db.find_one(collection=collection, query={'token': token})
    q = dict(q)
    handler = q['SECRET_LINE']
    handler = WebhookHandler(handler)
    with open('static/line_log.json', 'w') as log_line:
        json.dump(raw_json, log_line)
    try:
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        events = raw_json['events'][0]
        _type = events['type']
        if _type == 'follow':
            userId = events['source']['userId']
            profile = get_profile(userId, q)
            inserted = {'displayName': profile['displayName'], 'userId': userId, 'img': profile['img'],
                        'status': profile['status']}
            db.insert_one(collection=f'line_follower{token}', data=inserted)
        elif _type == 'unfollow':
            userId = events['source']['userId']
            db.delete_one(f'line_follower{token}', query={'userId': userId})
        elif _type == 'postback':
            event_postback(events, q)
        elif _type == 'message':
            message_type = events['message']['type']
            if message_type == 'text':
                try:
                    userId = events['source']['userId']
                    message = events['message']['text']
                    profile = get_profile(userId, q)
                    push_message = {'user_id': userId, 'message': message, 'display_name': profile['displayName'],
                                    'img': profile['img'],
                                    'status': profile['status'], 'access_token': q['ACCESS_TOKEN']}
                    db.insert_one(collection='message_user', data=push_message)
                    handler.handle(body, signature)
                    handler_message(events, q)
                except InvalidSignatureError as v:
                    api_error = {'status_code': v.status_code, 'message': v.message}
                    return jsonify(api_error), 400
            else:
                no_event = len(raw_json['events'])
                for i in range(no_event):
                    events = raw_json['events'][i]
                    event_handler(events, q)
    except IndexError:
        return jsonify({'index': None}), 200
    return jsonify(raw_json)


def event_handler(events, q):
    line_bot_api = q['ACCESS_TOKEN']
    line_bot_api = LineBotApi(line_bot_api)
    replyToken = events['replyToken']
    package_id = '446'
    stickerId = randint(1988, 2027)
    line_bot_api.reply_message(replyToken, StickerSendMessage(package_id, str(stickerId)))


def event_postback(events, q):
    pass


def flex_client(alt_text: str, contents: dict):
    flex_custom = FlexSendMessage(
        alt_text=alt_text,
        contents=contents
    )
    return flex_custom


def handler_message(events, q):
    line_bot_api = q['ACCESS_TOKEN']
    line_bot_api = LineBotApi(line_bot_api)
    text = events['message']['text']
    reply = events['replyToken']
    user_id = events['source']['userId']
    data_intent = intent_model(text, q['ACCESS_TOKEN'])
    intent_name = data_intent['name']
    label = data_intent['predict'][0]
    choice_answers = data_intent['answers']
    contents = data_intent['contents']
    type = data_intent['type']
    confident = data_intent['confident'][0] * 100

    if data_intent.get('require'):
        line_bot_api.reply_message(reply, TextSendMessage(text=data_intent.get('require')))
    check_keyword = db.find_one(collection='match_rule_based', query={'keyword': text})
    if not check_keyword:
        if confident > 69:
            if text == 'ขอข้อมูลผลิตภัณฑ์':
                line_bot_api.reply_message(reply, card.mango_products())

            if type:
                contents = json.loads(contents)
                flex_custom = flex_client(alt_text=intent_name, contents=contents)
                line_bot_api.reply_message(reply, flex_custom)
            elif not type:
                choice = random.choice(choice_answers[label])
                line_bot_api.reply_message(reply, TextSendMessage(text=choice))
        else:
            line_bot_api.reply_message(reply, TextSendMessage(text='ฉันไม่เข้าใจ'))
    elif check_keyword:
        alt_text = check_keyword['name']
        contents = check_keyword['contents']
        status = check_keyword['status']
        if status:
            contents = json.loads(contents)
            flex_custom = flex_client(alt_text=alt_text, contents=contents)
            line_bot_api.reply_message(reply, flex_custom)
        elif not status:
            line_bot_api.reply_message(reply, TextSendMessage(text=contents))
