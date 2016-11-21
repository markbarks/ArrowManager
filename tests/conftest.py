# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""
import os

import pytest
from webtest import TestApp

from arrowmanager.app import create_app
from arrowmanager.database import db as _db
from arrowmanager.settings import TestConfig

from .factories import GroupFactory, ApplicationFactory, UserFactory


@pytest.yield_fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app(TestConfig)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def testapp(app):
    """A Webtest app."""
    return TestApp(app)


@pytest.yield_fixture(scope='function')
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()


@pytest.fixture
def group(db):
    """A group for the tests."""
    group = GroupFactory()
    db.session.commit()
    return group


@pytest.fixture
def application(db):
    """A application for the tests."""
    application = ApplicationFactory()

    db.session.commit()
    return application


@pytest.fixture
def user(db):
    """A application for the tests."""
    user = UserFactory()

    db.session.commit()
    return user


@pytest.fixture
def client(app):
    """Creates a flask.Flask test_client object
    :app: fixture that provided the flask.Flask app
    :returns: flask.Flask test_client object
    """

    return app.test_client()


@pytest.fixture
def k8s():
    from k8sclient.client import api_client
    from k8sclient.client.apis import apiv_api
    from tests.integration.test_k8sclient import K8S_ENDPOINT

    k8s_conf = os.path.join(os.path.expanduser('~'), '.minikube')
    k8s = api_client.ApiClient(host=K8S_ENDPOINT,
                                      key_file=os.path.join(k8s_conf, 'apiserver.key'),
                                      cert_file=os.path.join(k8s_conf, 'apiserver.crt'),
                                      ca_certs=os.path.join(k8s_conf, 'ca.crt'))
    return apiv_api.ApivApi(k8s)
