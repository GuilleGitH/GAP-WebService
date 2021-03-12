import uuid
import datetime

from src.main import db
from src.main.model.harvest_form import HarvestForm


def complete_prediction(field):
    harvestForm = HarvestForm("date", "time", "plot", "note", "product", "quantity")
    response = harvestForm.makePrediction(field)
    return response, 200 
