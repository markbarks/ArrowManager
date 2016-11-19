from flask import Blueprint
from flask_restful import Api

from . import resources

blueprint = Blueprint('arrows', __name__)
api = Api(blueprint, prefix='/api')

api.add_resource(resources.ArrowsAPI, '/arrows')
api.add_resource(resources.ArrowAPI, '/arrow', '/arrow/<arrow_id>')
