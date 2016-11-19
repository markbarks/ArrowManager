from flask import Blueprint
from flask import request, jsonify
from flask_jwt_extended import create_access_token

from arrowmanager.models import User

auth = Blueprint('auth', __name__, url_prefix='/api')


# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token

@auth.route('/auth', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        # Identity can be any data that is json serializable
        ret = {'access_token': create_access_token(identity=username)}
        return jsonify(ret), 200

    return jsonify({"msg": "Bad username or password"}), 401
