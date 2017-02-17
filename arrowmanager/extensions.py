# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CsrfProtect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

bcrypt = Bcrypt()
csrf_protect = CsrfProtect()
jwt = JWTManager()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
CORS = CORS()
