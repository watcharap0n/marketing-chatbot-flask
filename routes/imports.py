from flask import request, jsonify, Blueprint, send_file
from flask_pydantic_spec import Response
from modules.Invalidate import InvalidUsage
import datetime
from bson import ObjectId
from config.object_str import CutId
from modules.swagger import api
from config.db import MongoDB
from modules.pandasModules import DataColumnFilter
from environ.client_environ import MONGODB_URI
import os

route_import = Blueprint('imports', __name__, template_folder='templates')

# client = 'mongodb://127.0.0.1:27017'
# client = os.environ.get('MONGODB_URI')
db = MongoDB(database_name='Mango', uri=MONGODB_URI)
collection = 'imports'


@route_import.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@route_import.route('/api/import', methods=['GET'])
@api.validate(resp=Response(HTTP_200=None, HTTP_400=None), tags=['Import'])
def get_customers():
    data = db.find(collection=collection, query={})
    data = list(data)
    for v in data:
        del v['_id']
    products = set([v['product'] for v in data if v['product']])
    channels = set([v['channel'] for v in data if v['channel']])
    tags = set([v['tag'][0] for v in data if v.get('tag')])
    return jsonify({
        'transaction': data[::-1],
        'products': list(products),
        'channels': list(channels),
        'tags': list(tags)
    })


@route_import.route('/api/import', methods=['POST'])
@api.validate(resp=Response(HTTP_201=None, HTTP_400=None), tags=['Import'])
def post_customer():
    data = request.get_json()
    key = CutId(_id=ObjectId()).dict()['id']
    _d = datetime.datetime.now()
    data["date"] = _d.strftime("%d/%m/%y")
    data["time"] = _d.strftime("%H:%M:%S")
    data["id"] = key
    db.insert_one(collection=collection, data=data)
    del data['_id']
    return jsonify(data)


@route_import.route('/api/import/<string:id>', methods=['PUT'])
@api.validate(resp=Response(HTTP_204=None, HTTP_400=None), tags=['Import'])
def put_customer(id):
    payload = request.get_json()
    _d = datetime.datetime.now()
    query = {'id': id}
    values = {'$set': payload}
    db.update_one(collection=collection, values=values, query=query)
    return jsonify({'message': 'success'})


@route_import.route('/api/import/<string:id>', methods=['DELETE'])
@api.validate(resp=Response(HTTP_204=None, HTTP_403=None), tags=['Import'])
def customer_delete(id):
    db.delete_one(collection=collection, query={'id': id})
    return jsonify({'message': 'success'})


@route_import.route('/api/import/delete/multiple', methods=['POST'])
@api.validate(resp=Response(HTTP_204=None, HTTP_403=None), tags=['Import'])
def customers_delete():
    items = request.get_json(force=True)
    for i in items:
        db.delete_one(collection=collection, query={'id': i['id']})
    res = {'message': 'success'}
    return jsonify(res)

@route_import.route('/api/m/sorting/', methods=['POST'])
@api.validate(resp=Response(HTTP_200=None, HTTP_403=None), tags=['Import'])
def customer_sorting():
    item = request.get_json()
    product = item['product']
    channel = item['channel']
    date = item['date']
    tag = item['tag']

    if not date:
        sorting = DataColumnFilter(collection=collection, database=db, product=product, channel=channel, tag=tag)
        dfs = sorting.filter()
        data = sorting.sorting_table(dfs=dfs)
        data = data.to_dict('records')
        return jsonify(data)

    sorting = DataColumnFilter(collection=collection, after_start_date=date[0], before_end_date=date[1], database=db,
                               product=product, channel=channel, tag=tag)
    dfs = sorting.filter()
    data = sorting.sorting_table(dfs=dfs)
    data = data.to_dict('records')
    return jsonify(data)


@route_import.route('/api/datafile/import/excel', methods=['POST'])
@api.validate(resp=Response(HTTP_200=None, HTTP_400=None), tags=['Import'])
def import_excel():
    id = request.get_json(force=True)
    excel = DataColumnFilter(id=id, database=db, collection=collection)
    excel.export_excel().save()
    file = os.path.join('static', 'excels/customers.xlsx')
    return send_file(file, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                     attachment_filename='customers.xlsx')
