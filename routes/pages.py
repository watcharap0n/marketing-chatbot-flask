from flask import Blueprint, render_template, url_for, redirect, request, current_app
from modules.swagger import api
from routes.secure import g

page = Blueprint('pages', __name__, template_folder='templates')


@page.route('/signin')
@api.validate(tags=['Page'])
def root_signIn():
    return render_template('admin/signin.vue')


@page.route('/')
@api.validate(tags=['Page'])
def root_customers():
    if g.user:
        return render_template('public/customers.vue')
    else:
        return redirect(url_for('pages.root_signIn'))


@page.route('/dashboard')
@api.validate(tags=['Page'])
def root_dashboard():
    if g.user:
        return render_template('public/dashboard.vue')
    else:
        return redirect(url_for('pages.root_signIn'))


@page.route('/intents')
@api.validate(tags=['Page'])
def root_intents():
    if g.user:
        return render_template('public/intents.vue')
    else:
        return redirect(url_for('pages.root_signIn'))


@page.route('/custom/form/<string:id>')
def line_custom(id):
    if g.user:
        return render_template('public/form_custom.vue', id=id)
    else:
        return redirect(url_for('pages.root_signIn'))


@page.route('/line/questionnaire/construction')
def line_construction():
    return render_template('LINE/construction.vue')


@page.route('/line/questionnaire/planing')
def line_planning():
    return render_template('LINE/planing.vue')


@page.route('/line/questionnaire/powerbi')
def line_powerbi():
    return render_template('LINE/powerbi.vue')


@page.route('/line/questionnaire/quote')
def line_quote():
    return render_template('LINE/quote.vue')


@page.route('/line/questionnaire/realestate')
def line_realestate():
    return render_template('LINE/reales.vue')


@page.route('/line/questionnaire/care')
def line_mangocare():
    return render_template('LINE/care.vue')


@page.route('/line/questionnaire/mg_home')
def line_mg_home():
    return render_template('LINE/mg_home.vue')


@page.route('/facebook/questionnaire/quotation')
def facebook_quotation():
    return render_template('FACEBOOK/quotation.vue')


@page.route('/custom/page/<string:id>')
def custom_page(id):
    return render_template('public/page_custom.vue', id=id)


@page.route('/root/mkt/notify/')
def root_mkt_notify():
    return render_template('notifyMKT/dashboard.vue')
