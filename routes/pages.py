from flask import Blueprint, render_template, url_for, redirect
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


@page.route('/intents')
@api.validate(tags=['Page'])
def root_intents():
    if g.user:
        return render_template('public/intents.vue')
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


@page.route('/facebook/questionnaire/quotation')
def facebook_quotation():
    return render_template('FACEBOOK/quotation.vue')
