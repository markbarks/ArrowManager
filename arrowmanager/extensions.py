# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_jwt import JWT

jwt = JWT()
db = SQLAlchemy()
cache = Cache()
