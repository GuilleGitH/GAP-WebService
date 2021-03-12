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

        }
        func = switcher.get(field, lambda: "Invalid month")

        response = {
            'status': 'prediction completed',
            'predicted_form': {
                'date': {
                    'pred1': 'pred1 - chance',
                    'pred2': 'pred2 - chance',
                },
                'time': 'self.time',
                'plot': 'self.plot',
                'note': 'self.note',
                'issue_type': 'self.issue_type',
                'description': 'self.description',
            }
        }
        return func()
