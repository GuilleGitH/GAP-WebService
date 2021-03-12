from .form_predictor import FormPredictor

class IssueFormPredictor(FormPredictor):

    def predict_type(self):
        prediction = {
            'status': 'prediction for type completed',
            'predicted_types':[
                {'type': 'acaros', 'chance': '90%'},
                {'type': 'hongos', 'chance': '70%'},
                {'type': 'insectos', 'chance': '50%'}
            ]
        }
        return prediction

    def predict_description(self):
        prediction = {
            'status': 'prediction for product completed',
            'predicted_description':[
                {'description': 'arañuela roja', 'chance': '90%'},
                {'description': 'tuta', 'chance': '70%'},
                {'description': 'fulvia', 'chance': '50%'}
            ]
        }
        return prediction

    def predict_complete_form(self):
        prediction = {
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
        return prediction