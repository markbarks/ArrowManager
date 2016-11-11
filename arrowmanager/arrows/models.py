from arrowmanager.database import Column, Model, SurrogatePK, db, reference_col, relationship


class Arrow(SurrogatePK, Model):
    """Arrow model """

    name = Column(db.String())
    image = Column(db.String())

    client = Column(db.String())  # todo: relationship
    project = Column(db.String())  # todo: relationship

    def to_json2(self):
        """Returns a json representantion of the user.
        :returns: a json object.

        """

        return {
            'id': str(self.id),
            'name': str(self.name),
            'image': self.image
        }
