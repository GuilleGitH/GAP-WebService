from .. import db, flask_bcrypt
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Density(db.Model):

    __tablename__ = 'density'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    crop = db.Column(db.String(255), nullable=False)
    density = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Crop '{}' - Density '{}'>".format(self.crop,self.density)
