from flask import Blueprint, render_template
from flask_stormpath import login_required

blueprint = Blueprint('dashboard', __name__, static_folder='../static', url_prefix='/dashboard')


@blueprint.route('/')
@login_required
def main():
    return render_template('dashboard/main.html')


@blueprint.route('/welcome/')
@login_required
def welcome():
    return render_template('dashboard/welcome.html')
