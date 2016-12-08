from flask import Blueprint, render_template
from flask_stormpath import login_required, current_user

from arrowmanager.arrows import controllers

blueprint = Blueprint('dashboard', __name__, static_folder='../static', url_prefix='/dashboard')


@blueprint.route('/', subdomain="<tenant>")
@login_required
def main(tenant):
    pods = controllers.get_pod_status(tenant)

    return render_template('dashboard/main.html',
                           tenant=tenant,
                           pods=pods)


@blueprint.route('/welcome/')
@login_required
def welcome():
    return render_template('dashboard/welcome.html')
