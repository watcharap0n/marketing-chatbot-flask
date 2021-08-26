from flask import request, jsonify, Blueprint, make_response, flash, redirect, url_for, session, g
from firebase_admin import auth
from modules.Invalidate import InvalidUsage
from environ.client_environ import set_firebase, set_authentication
from environ.config_db import Config_firebase
from modules.swagger import api
from datetime import timedelta
import os

secure = Blueprint('secure', __name__, template_folder='templates')
config = Config_firebase(path_db=set_firebase, path_auth=set_authentication)
pb = config.authentication()
db = config.database_fb()


@secure.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@secure.route('/secure/register', methods=['POST'])
@api.validate(tags=['Secure'])
def register():
    try:
        file = request.files['file']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        filename = file.filename
        upload_dir = os.path.join('static', 'uploads')
        file_input = os.path.join(upload_dir, file.filename)
        http = f'https://mangoconsultant.net/static/uploads/{filename}'
        user = auth.create_user(
            email=email,
            password=password,
            display_name=username,
            photo_url=http
        )
        if file:
            file.save(file_input)
        return jsonify(user.__dict__)
    except auth.EmailAlreadyExistsError:
        raise InvalidUsage(message='your register already exists', status_code=400)


@secure.route('/secure/login', methods=['POST'])
@api.validate(tags=['Secure'])
def login():
    try:
        email = request.form['email']
        password = request.form['password']
        remember = request.form.getlist('remember')
        user = pb.sign_in_with_email_and_password(email, password)
        check_verify = auth.get_user_by_email(user['email'])
        if check_verify.email_verified:
            if len(remember) > 0:
                expires_token = 60 * 60 * 1
                expires_remember = 60 * 60 * 24 * 5
                auth_cookie = auth.create_session_cookie(id_token=user['idToken'], expires_in=timedelta(hours=1))
                content = {'url': '/', 'status': True, 'detail': 'login success'}
                response = make_response(content)
                response.set_cookie('hash_email', email, max_age=expires_remember)
                response.set_cookie('hash_password', password, max_age=expires_remember)
                response.set_cookie('remember', str(remember), max_age=expires_remember)
                response.set_cookie('access_token', str(auth_cookie), max_age=expires_token)
                flash('You were successfully logged in')
                return response
            else:
                expires_token = 60 * 60 * 1
                auth_cookie = auth.create_session_cookie(id_token=user['idToken'], expires_in=timedelta(hours=1))
                content = {'url': '/', 'status': True, 'detail': 'login success'}
                response = make_response(content)
                response.set_cookie(key='access_token', value=str(auth_cookie), max_age=expires_token)
                flash('You were successfully logged in')
                return response
        elif not check_verify.email_verified:
            pb.send_email_verification(user['idToken'])
            return {'status': False, 'detail': 'email verification'}
    except:
        raise InvalidUsage(message='your register already exists', status_code=400,
                           payload={'error': True})


@secure.route('/secure/read')
@api.validate(tags=['Secure'])
def read():
    if g.user:
        try:
            access_token = request.cookies.get('access_token')
            check = auth.verify_session_cookie(access_token)
            auth.revoke_refresh_tokens(check['sub'])
            return jsonify(check)
        except auth.InvalidSessionCookieError:
            raise InvalidUsage(message='auth Invalid SessionCookie Error', status_code=403)
        except:
            raise InvalidUsage(message='Something Wrong!', status_code=403)


@secure.route('/secure/cookie_login')
@api.validate(tags=['Secure'])
def remember_cookie():
    email = request.cookies.get('hash_email')
    password = request.cookies.get('hash_password')
    remember = request.cookies.get('remember')
    data = {'email': email, 'password': password, 'remember': remember}
    return jsonify(data)


@secure.route('/secure/logout')
@api.validate(tags=['Secure'])
def logout():
    session.clear()
    g.user = None
    res = redirect(url_for('pages.root_signIn'))
    res.set_cookie('access_token', max_age=0)
    return res



