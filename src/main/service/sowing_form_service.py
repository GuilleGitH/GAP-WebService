import uuid
import datetime

from src.main import db
from src.main.model.sowing_form import SowingForm


def complete_prediction(field):
    sowingForm = SowingForm("date", "time", "plot", "note", "lechuga", "quantity", "dose", "machine", "expected_yield")
    response = sowingForm.makePrediction(field)
    return response, 200
