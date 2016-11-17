# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import PostGenerationMethodCall, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory

from arrowmanager.database import db
from arrowmanager.models import Group, User, Application


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class GroupFactory(BaseFactory):
    """User factory."""

    name = Sequence(lambda n: 'name{0}'.format(n))

    class Meta:
        """Factory configuration."""
        model = Group


class ApplicationFactory(BaseFactory):
    """User factory."""

    name = Sequence(lambda n: 'name{0}'.format(n))
    repo = Sequence(lambda n: 'http://repo{0}.git'.format(n))
    group = SubFactory(GroupFactory)

    class Meta:
        """Factory configuration."""
        model = Application


class UserFactory(BaseFactory):
    """User factory."""

    username = Sequence(lambda n: 'user{0}'.format(n))
    email = Sequence(lambda n: 'user{0}@example.com'.format(n))
    password = PostGenerationMethodCall('set_password', 'example')
    active = True

    class Meta:
        """Factory configuration."""
        model = User
