from .form import Form


class IssueForm(Form):
    def __init__(self, date, time, plot, note, issue_type, description):
        super().__init__(date, time, plot, note)
        self.type = issue_type
        self.description = description

    def makePrediction():
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
        return response
