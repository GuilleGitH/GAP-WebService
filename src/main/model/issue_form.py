from .form import Form
from .predictors.issue_form_predictor import IssueFormPredictor 

class IssueForm(Form):
    def __init__(self, date, time, plot, note, issue_type, description):
        super().__init__(date, time, plot, note)
        self.type = issue_type
        self.description = description
        self.predictor = IssueFormPredictor()

    def makePrediction(self, field): 
        switcher = {
            'type': self.predictor.predict_type,
            'description': self.predictor.predict_description,
            'all': self.predictor.predict_complete_form
        }
        func = switcher.get(field, lambda: "Invalid month")
        return func()
