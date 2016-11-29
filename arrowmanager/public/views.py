# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, render_template, request
from flask_stormpath.forms import LoginForm

blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/', subdomain="www")
def home():
    """Home page."""
    form = LoginForm(request.form)
    return render_template('public/home.html', form=form)


@blueprint.route('/about/', subdomain="www")
def about():
    """About page."""
    return render_template('public/about.html')
