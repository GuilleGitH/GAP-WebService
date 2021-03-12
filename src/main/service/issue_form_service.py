import uuid
import datetime

from src.main import db
from src.main.model.issue_form import IssueForm


def complete_prediction(field):
    issueForm = IssueForm("date", "time", "plot", "note", "product", "quantity")
    response = issueForm.makePrediction(field)
    return response, 200 
