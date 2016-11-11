from flask import Blueprint
from arrowmanager import helpers
from . import resources


blueprint = Blueprint('deployments', __name__)
api = helpers.MyApi(blueprint, prefix='/api')

api.add_resource(resources.ArrowsAPI, '/deployments')
api.add_resource(resources.ArrowAPI, '/arrow', '/arrow/<arrow_id>')
