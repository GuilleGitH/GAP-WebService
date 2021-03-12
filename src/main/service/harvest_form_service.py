import uuid
import datetime

from src.main import db
from src.main.model.harvest_form import HarvestForm


def complete_prediction():
    response = HarvestForm.makePrediction()
    return response, 200
