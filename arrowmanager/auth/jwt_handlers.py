import datetime
from flask import current_app
from arrowmanager import helpers, models


def set_jwt_handlers(jwt):
    """Define handlers to jwt.

    :jwt: flask_jwt.JWT object
    :returns: None

    """
    @jwt.authentication_handler
    def authenticate(username, password):
        user = models.User.objects(username=username).first()

        if user and helpers.verify_password(password, user.password):
            return user
        return None

    @jwt.identity_handler
    def identify(payload):
        return models.User.objects(id=payload['user_id']).first()

    @jwt.jwt_error_handler
    def error_handler(error):
        return 'Auth Failed: {}'.format(error.description), 400

    @jwt.jwt_payload_handler
    def make_payload(user):
        return {
            'user_id': str(user.id),
            'exp': (datetime.datetime.utcnow() +
                    current_app.config['JWT_EXPIRATION_DELTA']).isoformat()
        }

