import uuid
from datetime import datetime

from src.data import db
from src.data.model.sow import Sow


def save_new_sow(data):

    d, m, y = data['date'].split('/')
    sow_date = datetime(int(y), int(m), int(d))

    new_sow = Sow(
        date=sow_date,
        crop=data['crop'],
        plot_id=data['plot'],
        unit=data['unit'],
        quantity=data['quantity'],
        time_to_harvest=sow_date,
        harvest_duration=data['harvest_duration'],
        expected_yield=data['expected_yield']
    )
    save_changes(new_sow)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered a new Sow.'
    }
    return response_object, 201


def get_all_sow():
    return Sow.query.all()


def get_a_sow(public_id):
    return Sow.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
