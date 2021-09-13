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
    return jsonify(res)


@route_dashboard.route('/api/chart/initialized')
@api.validate(tags=['Chart'])
def chart():
    collection = request.args.get('collection')
    module = DataColumnFilter(database=db, collection=collection)
    df = module.filter_datetime_time_of_day()
    res = module.filter_of_chart(df=df)
    res = res.to_dict('records')
    return jsonify(res)


@route_dashboard.route('/api/chart/monthly')
@api.validate(tags=['Chart'])
def chart_monthly():
    collection = request.args.get('collection')
    module = DataColumnFilter(database=db, collection=collection)
    df = module.filter_datetime_time_of_day()
    CH = ['GetDemo', 'LINE', 'Contact']
    lst = []
    for i in CH:
        res = module.filter_of_chart(df=df, condition=True, of_monthly=True, year=2021, channel=i)
        res = res.to_dict('records')
        lst.append(res)
    return jsonify(lst)


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
    return jsonify(res)
