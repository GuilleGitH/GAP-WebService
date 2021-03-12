import uuid
import datetime

from src.main import db
from src.main.model.sowing_form import SowingForm


def complete_prediction():
    response = SowingForm.makePrediction()
    return response, 200
