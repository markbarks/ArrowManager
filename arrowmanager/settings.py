# -*- coding: utf-8 -*-
"""Application configuration."""
import os

import datetime


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('GRIDARROW_SECRET', 'st3vi3kinscoll0sus')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STORMPATH_API_KEY_FILE = os.path.expanduser("~/.stormpath/apiKey-5HWFFDZCO9E7OJK2IO8EKW298.properties")
    STORMPATH_APPLICATION = 'Gridarrow'

    STORMPATH_REDIRECT_URL = '/dashboard/'
    STORMPATH_REGISTRATION_REDIRECT_URL = '/dashboard/welcome'

    # JWT_AUTH_URL_RULE = '/api/auth'
    # JWT_EXPIRATION_DELTA = datetime.timedelta(days=1)
    # HASH_ALGORITHM = 'SHA512'
    # HASH_SALT = 'StevieTheWonderCat'


# This API Key wase Client automatically created for Application "Gridarrow"
#     to be used from th API. Disabling or deleting this key can impact your
#     application.

class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'  # TODO: Change me
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing
