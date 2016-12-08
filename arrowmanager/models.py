from arrowmanager.database import SurrogatePK, Model, Column
from arrowmanager.database import reference_col, relationship
from arrowmanager.extensions import db


class Application(SurrogatePK, Model):
    __tablename__ = 'application'

    tenant = Column(db.String(), nullable=False)

    name = Column(db.String(), nullable=False)
    repo = Column(db.String(), nullable=False)

    builds = relationship('Build', back_populates='application')

    def __init__(self, name, tenant, repo, **kwargs):
        """Create instance."""
        db.Model.__init__(self, tenant=tenant, name=name, repo=repo,
                          **kwargs)

        # tags =
        # deployments = relationship('Deployment', back_populates='application')

    def __repr__(self):
        return "{} / {}".format(self.name, self.repo)



class Build(SurrogatePK, Model):
    __tablename__ = 'build'

    tenant = Column(db.String(), nullable=False)

    git_rev = Column(db.String(), nullable=False)
    image = Column(db.String(), nullable=False)
    buildtime = Column(db.DateTime(), nullable=False)

    # Probably Jenkins build number etc

    application_id = reference_col('application', nullable=False)
    application = relationship('Application', back_populates='builds')

    def __init__(self, application, image, git_rev, buildtime, **kwargs):
        """Create instance."""
        db.Model.__init__(self, tenant=application.tenant,
                          application=application,
                          image=image,
                          git_rev=git_rev,
                          buildtime=buildtime, **kwargs)

    def __repr__(self):
        return "{} / {}".format(self.image, self.buildtime)

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
