from flask import Blueprint, render_template

from arrowmanager.arrows import controllers

blueprint = Blueprint('dashboard', __name__,
                      static_folder='../static',
                      url_prefix='/dashboard')


@blueprint.route('/')
def main():
    tenant = 'megacorp'

    pods = controllers.get_pod_status(tenant)

    applications = controllers.get_applications(tenant)

    return render_template('dashboard/main.html',
                           tenant=tenant,
                           applications=applications,
                           pods=pods)


@blueprint.route('/welcome/')
def welcome():
    return render_template('dashboard/welcome.html')
