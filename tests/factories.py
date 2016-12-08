# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import PostGenerationMethodCall, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory

from arrowmanager.database import db
from arrowmanager.models import Application


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session



class ApplicationFactory(BaseFactory):
    """User factory."""

    tenant = 'deafult'
    name = Sequence(lambda n: 'name{0}'.format(n))
    repo = Sequence(lambda n: 'http://repo{0}.git'.format(n))
    # group = SubFactory(GroupFactory)

    class Meta:
        """Factory configuration."""
        model = Application


