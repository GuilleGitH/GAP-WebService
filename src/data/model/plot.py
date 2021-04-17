from .. import db, flask_bcrypt
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Plot(db.Model):

    __tablename__ = 'plot'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    area = db.Column(db.Float, nullable=False)
    sow = relationship("Sow")
    issue = relationship("Issue")
    application = relationship("Application")
    harvest = relationship("Harvest")
