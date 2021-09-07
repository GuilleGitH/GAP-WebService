import uuid
import datetime

from src.main import db
from src.main.model.sowing_form import SowingForm


def complete_prediction(data, field_required):
    print(data)
    sowingForm = SowingForm(data['date'], 'asd', data['plot'], 'asdad', data['crop'], data['quantity'], data['time_to_harvest'], data['harvest_duration'], data['expected_yield'], data['unit'])
    response = sowingForm.makePrediction(field_required)
    return response, 200
