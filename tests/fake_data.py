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


if __name__ == '__main__':
    with app() as a, db(a):
        application = Application(tenant='default',
                                  name='TwExcel',
                                  repo='https://github.com/markbarks/AlderExamples.git')
        application.save()

        build = Build(application=application,
                      image="eu.gcr.io/gridarrow/twexcel:1",
                      git_rev='646df370f851479d7423da324ec0b09116335584',
                      buildtime=datetime.now())
        build.save()

        build = Build(application=application,
                      image="eu.gcr.io/gridarrow/twexcel:2",
                      git_rev='62419c58e12d242b9521a89ffcc390593e721569',
                      buildtime=datetime.now() + timedelta(hours=1))
        build.save()

        application = Application(tenant='default',
                                  name='Quandlex',
                                  repo='https://github.com/markbarks/AlderExamples.git')
        application.save()

        build = Build(application=application,
                      image="eu.gcr.io/gridarrow/quandlex:1",
                      git_rev='646df370f851479d7423da324ec0b09116335584',
                      buildtime=datetime.now())
        build.save()

        build = Build(application=application,
                      image="eu.gcr.io/gridarrow/quandlex:2",
                      git_rev='62419c58e12d242b9521a89ffcc390593e721569',
                      buildtime=datetime.now() + timedelta(minutes=30))
        build.save()
