from contextlib import contextmanager
from datetime import datetime, timedelta

from arrowmanager.app import create_app
from arrowmanager.database import db as _db
from arrowmanager.models import Build, Application
from arrowmanager.settings import DevConfig


@contextmanager
def app():
    """An application for the tests."""
    _app = create_app(DevConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@contextmanager
def db(app):
    """A database for the tests."""
    _db.app = app

    yield _db

    # Explicitly close DB connection
    _db.session.close()

