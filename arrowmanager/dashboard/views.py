from flask import Blueprint, render_template
from flask_stormpath import login_required, current_user

from arrowmanager.arrows import controllers

blueprint = Blueprint('dashboard', __name__, static_folder='../static', url_prefix='/dashboard')


@blueprint.route('/', subdomain="<organization>")
@login_required
def main(organization):
    pods = controllers.get_pod_status(organization)

    return render_template('dashboard/main.html',
                           organization=organization,
                           pods=pods)


@blueprint.route('/welcome/')
@login_required
def welcome():
    return render_template('dashboard/welcome.html')
