from flask import request, jsonify, Blueprint, send_file
from modules.Invalidate import InvalidUsage
from modules.swagger import api
from config.db import MongoDB
from modules.pandasModules import DataColumnFilter
from environ.client_environ import MONGODB_URI
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from wordcloud import WordCloud
from pythainlp.tokenize import word_tokenize
import pandas as pd

route_dashboard = Blueprint('dashboard', __name__, template_folder='templates')

db = MongoDB(database_name='Mango', uri=MONGODB_URI)


@route_dashboard.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@route_dashboard.route('/api/chart/daly', methods=['POST'])
@api.validate(tags=['Chart'])
def chart_condition():
    collection = request.args.get('collection')
    item = request.get_json()
    module = DataColumnFilter(database=db, collection=collection)
    df = module.filter_datetime_time_of_day()
    res = module.filter_of_chart(df=df, year=2021, condition=True,
                                 month=item['month'], channel=item['channel'])
    res = res.to_dict('records')
    new_data = []
    name = []
    cate = []
    data = []
    new_dict = {}
    for v in res:
        v['name'] = v.pop('channel')
        v['data'] = v.pop('count')
        v['categories'] = v.pop('day')
        name.append(v['name'])
        cate.append(f'day {v["categories"]}')
        data.append(v['data'])
    try:
        new_dict['name'] = name[0]
    except IndexError:
        new_dict['name'] = ''
    new_dict['categories'] = cate
    new_dict['data'] = data
    new_data.append(new_dict)
    return jsonify(new_data)


@route_dashboard.route('/api/chart/initialized')
@api.validate(tags=['Chart'])
def chart():
    collection = request.args.get('collection')
    module = DataColumnFilter(database=db, collection=collection)
    df = module.filter_datetime_time_of_day()
    res = module.filter_of_chart(df=df)
    res = res.to_dict('records')
    return jsonify(res)


@route_dashboard.route('/api/chart/monthly', methods=['POST'])
@api.validate(tags=['Chart'])
def chart_monthly():
    # CH = request.get_json(force=True)
    collection = request.args.get('collection')
    year = 2021
    arg_year = request.args.get('year')
    if arg_year:
        year = int(arg_year)
    module = DataColumnFilter(database=db, collection=collection)
    df = module.filter_datetime_time_of_day()
    CH = ['GetDemo', 'LINE', 'Contact']
    new_data = []
    for i in CH:
        name = []
        cate = []
        data = []
        new_dict = {}
        res = module.filter_of_chart(df=df, condition=True, of_monthly=True, year=year, channel=i)
        res = res.to_dict('records')
        for v in res:
            v['name'] = v.pop('channel')
            v['data'] = v.pop('count')
            v['categories'] = v.pop('month')
            name.append(v['name'])
            cate.append(f'month {v["categories"]}')
            data.append(v['data'])
        try:
            new_dict['name'] = name[0]
        except IndexError:
            new_dict['name'] = ''
        new_dict['categories'] = cate
        new_dict['data'] = data
        new_data.append(new_dict)
    return jsonify(new_data)


@route_dashboard.route('/api/chart/productAndChannel', methods=['POST'])
@api.validate(tags=['Chart'])
def chart_product_and_channel():
    collection = request.args.get('collection')
    item = request.get_json()
    module = DataColumnFilter(database=db, collection=collection)
    df = module.filter_datetime_time_of_day()
    res = module.filter_of_chart(df=df, condition=True, of_months_products=True,
                                 year=2021, channel=item['channel'], product=item['product'])
    res = res.to_dict('records')
    new_data = []
    name = []
    cate = []
    data = []
    new_dict = {}
    for v in res:
        v['name'] = v.pop('channel')
        v['data'] = v.pop('count')
        v['categories'] = v.pop('month')
        name.append(v['name'])
        cate.append(f'month {v["categories"]}')
        data.append(v['data'])
    try:
        new_dict['name'] = name[0]
    except IndexError:
        new_dict['name'] = ''
    new_dict['categories'] = cate
    new_dict['data'] = data
    new_data.append(new_dict)
    return jsonify(new_data)


@route_dashboard.route('/api/chart/wordCloud')
@api.validate(tags=['Chart'])
def chart_wordCloud():
    data = db.find(collection='message_user', query={})
    data = list(data)
    texts = [x['message'] for x in data]
    regexp = r"[ก-๙a-zA-Z']+"
    vectorized = CountVectorizer(tokenizer=word_tokenize)
    df = pd.DataFrame(columns=['name', 'count'])
    transform_data = vectorized.fit_transform(texts)
    count = np.ravel(transform_data.sum(axis=0))
    vector_name = vectorized.get_feature_names()
    df['count'] = count
    df['name'] = vector_name
    data = df.sort_values(by=['count'], ascending=False)
    data = data.drop(0)
    data.plot(kind='bar', figsize=(12, 6))
    word_dict = {}
    for i in range(1, len(data)):
        word_dict[data.name[i]] = data['count'][i]
    font_path = 'static/tools/THSarabunNew.ttf'
    wordcloud = WordCloud(
        font_path=font_path,
        relative_scaling=0.3,
        min_font_size=1,
        background_color="white",
        width=1024,
        height=768,
        max_words=2000,
        colormap='plasma',
        scale=3,
        font_step=4,
        #   contour_width=3,
        #   contour_color='steelblue',
        collocations=False,
        regexp=regexp,
        margin=2
    ).fit_words(word_dict)
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    fig.savefig('static/uploads/word.png')
    plt.close(fig)
    return send_file('static/uploads/word.png', mimetype='image/gif')
