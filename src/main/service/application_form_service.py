import uuid
import datetime

from src.main import db
from src.main.model.application_form import ApplicationForm


def complete_prediction():
    response = ApplicationForm.makePrediction()
    return response, 200
