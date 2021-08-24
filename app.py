"""
check the document at URL location /apidoc/redoc or /apidoc/swagger
"""

from flask import Flask, jsonify, session, g
from modules.swagger import api
from routes import customers, imports, intents, tags, wh_client, secure, pages, questionnaires, wh_mango, ruleBased, \
    wh_notify, api_cors
from flask_cors import CORS
from datetime import timedelta
from modules.Invalidate import InvalidUsage

app = Flask(__name__)

cors = CORS(app, resources={r'/api/*': {'origins': '*'}})
app.secret_key = 'watcharaponweeraborirakz'


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.before_request
def before_request():
    try:
        if 'user_id' in session:
            user = session['user_id']['idToken']
            g.user = user
        else:
            g.user = None
    except:
        raise InvalidUsage(status_code=403, message='authentication error')


@app.before_request
def make_session_permanent():
    session.permanent = True
    secure.permanent_session_lifetime = timedelta(minutes=60)


app.register_blueprint(
    customers.route_customer
)
app.register_blueprint(
    imports.route_import
)
app.register_blueprint(
    intents.route_intent
)
app.register_blueprint(
    tags.route_tag
)
app.register_blueprint(
    wh_client.route_callback
)
app.register_blueprint(
    secure.secure
)
app.register_blueprint(
    pages.page
)
app.register_blueprint(
    questionnaires.question
)
app.register_blueprint(
    wh_mango.route_callback_mango
)
app.register_blueprint(
    ruleBased.rule_base
)
app.register_blueprint(
    api_cors.public,
)
app.register_blueprint(
    wh_notify.notify
)

if __name__ == "__main__":
    api.register(app)  # if you don't register in api init step
    app.run(port=7000, debug=True)
