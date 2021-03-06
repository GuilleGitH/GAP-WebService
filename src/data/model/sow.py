from .. import db, flask_bcrypt
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .plot import Plot

Base = declarative_base()


class Sow(db.Model):

    __tablename__ = 'sow'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    plot_id = db.Column(db.Integer, ForeignKey('plot.id'))
    crop = db.Column(db.String(255), nullable=False)
    unit = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    time_to_harvest = db.Column(db.DateTime, nullable=False)
    harvest_duration = db.Column(db.Integer, nullable=False)
    expected_yield = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<User '{}'>".format(self.name)
