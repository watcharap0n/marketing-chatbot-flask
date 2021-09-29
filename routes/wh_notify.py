from flask import request, jsonify, Blueprint
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import StickerSendMessage, TextSendMessage, TextMessage, MessageEvent
from random import randint
from modules.Invalidate import InvalidUsage
from environ.line_token import line_bot_api, handler
from config.db import MongoDB
from environ.client_environ import MONGODB_URI
import json
import os
from bson import ObjectId
from config.object_str import CutId
import datetime

notify = Blueprint('callback_notify', __name__, template_folder='templates')

# client = os.environ.get('MONGODB_URI')
db = MongoDB(database_name='Mango', uri=MONGODB_URI)
collection = 'line_bot_notify'

line_bot_api_notify = LineBotApi(line_bot_api)
handler_notify = WebhookHandler(handler)


@notify.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def get_profile_notify(user_id):
    profile = line_bot_api_notify.get_profile(user_id)
    displayName = profile.display_name
    userId = profile.user_id
    img = profile.picture_url
    status = profile.status_message
    key = CutId(_id=ObjectId()).dict()['id']
    _d = datetime.datetime.now()
    date = _d.strftime("%d/%m/%y")
    time = _d.strftime("%H:%M:%S")
    result = {
        'displayName': displayName,
        'userId': userId,
        'img': img,
        'status': status,
        'id': key,
        'date': date,
        'time': time
    }
    return result


@notify.route('/callback/token/notifyMKT', methods=['POST'])
def callback_notify():
    raw_json = request.get_json()
    with open('log/notify_log.json', 'w') as log_line:
        json.dump(raw_json, log_line)
    try:
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        events = raw_json['events'][0]
        _type = events['type']
        if _type == 'follow':
            userId = events['source']['userId']
            profile = get_profile_notify(userId)
            db.insert_one(collection='line_follower_notify', data=profile)
        elif _type == 'unfollow':
            userId = events['source']['userId']
            db.delete_one('line_follower_notify', query={'userId': userId})
        elif _type == 'postback':
            event_postback_notify(events)
        elif _type == 'message':
            message_type = events['message']['type']
            if message_type == 'text':
                try:
                    handler_notify.handle(body, signature)
                except InvalidSignatureError as v:
                    raise InvalidUsage(message=v.message, status_code=400)
            else:
                no_event = len(raw_json['events'])
                for i in range(no_event):
                    events = raw_json['events'][i]
                    event_handler_notify(events)
    except IndexError:
        raise InvalidUsage(message='index null', status_code=200)
    return jsonify(raw_json)


def event_handler_notify(event):
    replyToken = event['replyToken']
    package_id = '446'
    stickerId = randint(1988, 2027)
    line_bot_api_notify.reply_message(replyToken, StickerSendMessage(package_id, str(stickerId)))


def event_postback_notify(event):
    pass


@handler_notify.add(MessageEvent, message=TextMessage)
def handler_message_notify(event):
    replyToken = event.reply_token
    message_text = event.message.text
    line_bot_api_notify.reply_message(replyToken, TextSendMessage(text=message_text))


@notify.route('/user_notify/<string:userId>/valid')
def valid_user(userId):
    user = db.find_one(collection='line_follower_notify', query={'userId': userId})
    if user:
        del user['_id']
        return jsonify(status=True, message='user in already!', data=user)
    else:
        user = get_profile_notify(userId)
        db.insert_one(collection='line_follower_notify', data=user)
        del user['_id']
        return jsonify(status=False, message='user not in already!', data=user), 201
