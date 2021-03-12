import uuid
import datetime

from src.main import db
from src.main.model.application_form import ApplicationForm


def complete_prediction(field):
    applicationForm = ApplicationForm("date", "time", "plot", "note", "product", "quantity", "dose", "machine")
    response = applicationForm.makePrediction(field)
    return response, 200  
