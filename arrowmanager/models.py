from datetime import datetime

from arrowmanager.database import SurrogatePK, Model, Column
from arrowmanager.database import reference_col, relationship
from arrowmanager.extensions import db, bcrypt


# class User(UserMixin, SurrogatePK, Model):
class User(SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = 'user'
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.Binary(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)

    def __init__(self, username, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    @cache.memoize(50)
    def has_membership(self, role_id):
        return Group.query.filter_by(user=self, role_id=role_id).count() >= 1


    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
        }

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)


class Group(SurrogatePK, Model):
    __tablename__ = 'group'

    name = Column(db.String())
    applications = relationship('Application', back_populates='group')

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)


class Application(SurrogatePK, Model):
    __tablename__ = 'application'

    name = Column(db.String())
    repo = Column(db.String())

    group_id = reference_col('group', nullable=False)
    group = relationship('Group', back_populates='applications')

    builds = relationship('Build', back_populates='application')

    def __init__(self, name, repo, group, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, repo=repo,
                          group=group, **kwargs)

        # tags =
        # deployments = relationship('Deployment', back_populates='application')


class Build(SurrogatePK, Model):
    __tablename__ = 'build'

    version = Column(db.String())
    image = Column(db.String())
    buildtime = Column(db.DateTime())

    application_id = reference_col('application', nullable=False)
    application = relationship('Application', back_populates='builds')

    def __init__(self, application, version, image, buildtime, **kwargs):
        """Create instance."""
        db.Model.__init__(self, application=application,
                          version=version, image=image,
                          buildtime=buildtime, **kwargs)

# class Deployment(SurrogatePK, Model):
#     __tablename__ = 'deployment'
#
#     application_id = reference_col('applications', nullable=False)
#     application = relationship('Application', back_populates='deployments')
#
#     build_id = reference_col('builds', nullable=False)
#     build = relationship('Build', back_populates='builds')
#
#     crontab = Column(db.String())
