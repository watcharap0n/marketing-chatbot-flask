from flask import request, jsonify, Blueprint, send_file
from modules.Invalidate import InvalidUsage
from modules.swagger import api
from config.db import MongoDB
from modules.pandasModules import DataColumnFilter
from environ.client_environ import MONGODB_URI

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
