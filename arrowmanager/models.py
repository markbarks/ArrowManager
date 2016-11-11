from arrowmanager.database import SurrogatePK, Model, Column
from arrowmanager.database import reference_col, relationship
from arrowmanager.extensions import db


class Group(SurrogatePK, Model):
    __tablename__ = 'groups'

    name = Column(db.String())
    applications = relationship('Application', back_populates='group')

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)


class Application(SurrogatePK, Model):
    __tablename__ = 'applications'

    name = Column(db.String())
    repo = Column(db.String())

    group_id = reference_col('groups', nullable=False)
    group = relationship('Group', back_populates='applications')

    builds = relationship('Build', back_populates='application')
    deployments = relationship('Deployment', back_populates='application')

    # tags =

    def to_json2(self):
        '''Returns a json representantion of the user.
        :returns: a json object.

        '''

        return {
            'id': str(self.id),
            'name': str(self.name),
            'image': self.image
        }


class Build(SurrogatePK, Model):
    __tablename__ = 'builds'

    version = Column(db.String())
    image = Column(db.String())
    buildtime = Column(db.DateTime())

    application_id = reference_col('applications', nullable=False)
    application = relationship('Application', back_populates='builds')


class Deployment(SurrogatePK, Model):
    __tablename__ = 'deployments'

    application_id = reference_col('applications', nullable=False)
    application = relationship('Application', back_populates='deployments')

    build_id = reference_col('builds', nullable=False)
    build = relationship('Build', back_populates='builds')

    crontab = Column(db.String())
