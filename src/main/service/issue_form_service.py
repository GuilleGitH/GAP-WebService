import uuid
import datetime

from src.main import db
from src.main.model.issue_form import IssueForm


def complete_prediction():
    response = IssueForm.makePrediction()
    return response, 200
