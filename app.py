"""
check the document at URL location /apidoc/redoc or /apidoc/swagger

application is run backend develop by watcharapon weeraborirak

github: watcharap0n

"""

import os
from datetime import timedelta
from flask import Flask, jsonify, session, g, request, current_app, render_template
from flask_cors import CORS
from routes import customers, imports, intents, tags, wh_client, secure, pages, \
    questionnaires, wh_mango, ruleBased, wh_notify, api_cors, dashboard
from modules.swagger import api
from modules.Invalidate import InvalidUsage
from routes.secure import auth

app = Flask(__name__)

cors = CORS(app, resources={r'/api/*': {'origins': '*'}})
app.secret_key = 'watcharaponweeraborirakz'


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    """

    :param error:
    :return:
    """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(404)
def page_not_found(error):
    """

    :param error:
    :return render_template(404):
    """
    current_app.logger.error("Page not found: %s", (request.path, error))
    return render_template("error_handle/404.html"), 404


@app.before_request
def before_request():
    """
    description: before render template javascript for the authentication -

    :return:
    """
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)
    try:
        access_token = request.cookies.get('access_token')
        check = auth.verify_session_cookie(access_token)
        auth.revoke_refresh_tokens(check['sub'])
        user = session['user_id'] = check
        g.user = user
    except auth.InvalidSessionCookieError:
        g.user = None
    except:
        g.user = None


@app.after_request
def after_request_func(response):
    """

    :param response:
    :return:
    """
    return response


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
    wh_notify.notifyMKT
)
app.register_blueprint(
    dashboard.route_dashboard
)
if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', 7000))
    api.register(app)  # if you don't register in api init step
    app.run(port=PORT, debug=True, use_reloader=True)
