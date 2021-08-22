from flask import request, jsonify, Blueprint
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import StickerSendMessage, TextSendMessage, QuickReplyButton, MessageAction, QuickReply, \
    MessageEvent, TextMessage, FlexSendMessage
from machine_leanning.model_text_classifire import intent_model
from features_line import card, flex_message
from random import randint
from config.db import MongoDB
from environ.line_token import mango_channel, mango_secret
from numpy import random
from environ.client_environ import MONGODB_URI
import logging
import json
import os

# client = 'mongodb://127.0.0.1:27017'
# client = os.environ.get('MONGODB_URI')
db = MongoDB(database_name='Mango', uri=MONGODB_URI)
collection = 'line_bot_mango'

route_callback_mango = Blueprint('callback_mango', __name__, template_folder='templates')

line_bot_api = LineBotApi(mango_channel)
handler = WebhookHandler(mango_secret)


def get_profile_mango(user_id):
    profile = line_bot_api.get_profile(user_id)
    displayName = profile.display_name
    userId = profile.user_id
    img = profile.picture_url
    status = profile.status_message
    result = {'displayName': displayName, 'userId': userId, 'img': img, 'status': status}
    return result


def quick_reply_custom(userId: str, send_text: str, labels: list, texts: list):
    line_bot_api.push_message(
        userId,
        TextSendMessage(
            text=send_text,
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=MessageAction(label=label, text=text)) for label, text in zip(labels, texts)
            ])
        )
    )


@route_callback_mango.route('/callback/token/mango', methods=['GET', 'POST'])
def webhookMango():
    if request.method == 'POST':
        raw_json = request.get_json()
        with open('log/webhook_mango.json', 'w') as webhook_mango:
            json.dump(raw_json, webhook_mango)
        try:
            signature = request.headers['X-Line-Signature']
            body = request.get_data(as_text=True)
            events = raw_json['events'][0]
            _type = events['type']
            if _type == 'follow':
                userId = events['source']['userId']
                profile = get_profile_mango(userId)
                inserted = {'displayName': profile['displayName'], 'userId': userId, 'img': profile['img'],
                            'status': profile['status']}
                db.insert_one(collection='line_follower', data=inserted)
                labels = ['ผลิตภัณฑ์แมงโก้', 'ขอใบเสนอราคา', 'สอบถามการอบรม', 'สอบถามการใช้งาน']
                texts = ['ผลิตภัณฑ์แมงโก้', 'ขอใบเสนอราคา', 'สอบถามการอบรม', 'สอบถามการใช้งาน']
                quick_reply_custom(
                    userId,
                    'สวัสดีค่ะ น้องแมงโก้ยินดีให้บริการท่านสามารถเลือกสอบถามเรื่องที่ท่านสนใจได้เลยค่ะ',
                    labels,
                    texts
                )
            elif _type == 'unfollow':
                userId = events['source']['userId']
                db.delete_one('line_follower', query={'userId': userId})
            elif _type == 'postback':
                event_postback_mango(events)
            elif _type == 'message':
                message_type = events['message']['type']
                if message_type == 'text':
                    try:
                        userId = events['source']['userId']
                        message = events['message']['text']
                        profile = get_profile_mango(userId)
                        push_message = {'user_id': userId, 'message': message, 'display_name': profile['displayName'],
                                        'img': profile['img'],
                                        'status': profile['status'], 'access_token': mango_channel}
                        db.insert_one(collection='message_user', data=push_message)
                        handler.handle(body, signature)
                    except InvalidSignatureError as v:
                        api_error = {'status_code': v.status_code, 'message': v.message}
                        return jsonify(api_error), 400
                else:
                    no_event = len(raw_json['events'])
                    for i in range(no_event):
                        events = raw_json['events'][i]
                        event_handler_mango(events)
        except IndexError:
            return jsonify({'index': None}), 200
        return jsonify(raw_json)


def event_postback_mango(event):
    reply = event['replyToken']
    postback = event['postback']['data']
    if postback == 'CSM' or postback == 'QCM' or postback == 'maintenance':
        line_bot_api.reply_message(reply, TextSendMessage(
            text='ผลิตภัณฑ์นี้เหมาะสำหรับบริษัทฯ ที่ใช้ Software ERP Mango Anywhere '
                 'เท่านั้น\nหากท่านสนใจใช้ สามารถติดต่อเจ้าหน้าที่ฝ่ายขาย\nได้ที่เบอร์ 063 565 4594 ค่ะ'))
    elif postback == 'team1':
        line_bot_api.reply_message(reply, flex_message.person_team_one())
    elif postback == 'team2':
        line_bot_api.reply_message(reply, flex_message.person_team_two())
    elif postback == 'team1_tel1':
        line_bot_api.reply_message(reply, TextSendMessage(text='084-551-1044'))
    elif postback == 'team1_tel2':
        line_bot_api.reply_message(reply, TextSendMessage(text='084-016-8454'))
    elif postback == 'team2_tel1':
        line_bot_api.reply_message(reply, TextSendMessage(text='086-956-5929'))
    elif postback == 'team2_tel2':
        line_bot_api.reply_message(reply, TextSendMessage(text='098-828-5742'))


def event_handler_mango(event):
    replyToken = event['replyToken']
    package_id = '446'
    stickerId = randint(1988, 2027)
    line_bot_api.reply_message(replyToken, StickerSendMessage(package_id, str(stickerId)))


def flex_mango(alt_text: str, contents: dict):
    flex_custom = FlexSendMessage(
        alt_text=alt_text,
        contents=contents
    )
    return flex_custom


@handler.add(MessageEvent, message=TextMessage)
def handler_message_mango(event):
    """
    handler event from API post webhook type text
    :param event:
    :return:
    """

    text = event.message.text
    reply = event.reply_token
    userId = event.source.user_id
    user = get_profile_mango(userId)
    displayName = user['displayName']

    data_intent = intent_model(text, mango_channel)
    intent_name = data_intent['name']
    label = data_intent['predict'][0]
    choice_answers = data_intent['answers']
    confident = data_intent['confident'][0] * 100
    logging.warning(intent_name)
    logging.warning(confident)

    if data_intent.get('require'):
        line_bot_api.reply_message(reply, TextSendMessage(text=data_intent.get('require')))
    check_keyword = db.find_one(collection='match_rule_based', query={'keyword': text})
    if not check_keyword:
        if confident > 69:
            """
            START ========================= FIX DEV =============================== 
            :exception next dev quick reply custom by user
            
            quick_name = 'สวัสดี'
            if quick_name == intent_name:
                labels = ['ผลิตภัณฑ์แมงโก้', 'ขอใบเสนอราคา', 'สอบถามการอบรม', 'สอบถามการใช้งาน']
                texts = ['ผลิตภัณฑ์แมงโก้', 'ขอใบเสนอราคา', 'สอบถามการอบรม', 'สอบถามการใช้งาน']
                quick_reply_custom(userId, 'สวัสดีจ้ายินดีให้บริการ', labels, texts)
            else:
                choice = random.choice(choice_answers[label])
                line_bot_api.reply_message(reply, TextSendMessage(text=choice))
                
            """

            if text == 'ขอข้อมูลผลิตภัณฑ์':
                line_bot_api.reply_message(reply, card.mango_products())

            """
            END ========================= FIX DEV =============================== 
            """
            choice = random.choice(choice_answers[label])
            line_bot_api.reply_message(reply, TextSendMessage(text=choice))
        else:

            """
            START ========================= FIX DEV NOT CONFIDENT =============================== 
            """

            """
            END ========================= FIX DEV NOT CONFIDENT =============================== 
            """
            line_bot_api.reply_message(reply, TextSendMessage(text='ฉันไม่เข้าใจ'))
    elif check_keyword:
        alt_text = check_keyword['name']
        contents = check_keyword['contents']
        status = check_keyword['status']
        if status:
            contents = json.loads(contents)
            flex_custom = flex_mango(alt_text=alt_text, contents=contents)
            line_bot_api.reply_message(reply, flex_custom)
        elif not status:
            line_bot_api.reply_message(reply, TextSendMessage(text=contents))
