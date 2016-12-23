from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from arrowmanager import helpers
from . import controllers


def post_put_parser():
    """Request parser for HTTP POST or PUT.
    :returns: flask.ext.restful.reqparse.RequestParser object

    """
    parse = reqparse.RequestParser()
    parse.add_argument(
        'username', type=str, location='json', required=True)
    parse.add_argument(
        'password', type=str, location='json', required=True)

    return parse


class ArrowsAPI(Resource):
    """An API to get or create users."""

    # @jwt_required
    # @helpers.standardize_api_response
    def get(self):
        """HTTP GET. Get one or all users.

        :username: a string valid as object id.
        :returns: One or all available users.

        """
        # namespace = get_jwt_identity()
        namespace = 'megacorp'

        return controllers.get_pod_status(namespace)

    @jwt_required
    @helpers.standardize_api_response
    def post(self):
        """HTTP POST. Create an user.

        :username: The user username
        :password: The user password (plaintext)
        :returns: The user id

        """

        parse = post_put_parser()
        args = parse.parse_args()
        username, password = args['username'], args['password']

        return controllers.create_or_update_user(username, password)


class ArrowAPI(Resource):
    """An API to update or delete an user. """

    @jwt_required
    @helpers.standardize_api_response
    def put(self):
        """HTTP PUT. Update an user.
        :returns:

        """

        parse = post_put_parser()
        parse.add_argument('user_id', type=str,
                           location='json', required=True)
        args = parse.parse_args()

        username, password = args['username'], args['password']
        user_id = args['user_id']

        return controllers.create_or_update_user(username,
                                                 password, user_id)

    @jwt_required
    @helpers.standardize_api_response
    def delete(self, user_id):
        """HTTP DELETE. Delete an user.
        :returns:

        """

        return controllers.delete_user(user_id)
