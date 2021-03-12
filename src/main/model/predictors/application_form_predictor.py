from .form_predictor import FormPredictor

class ApplicationFormPredictor(FormPredictor):

    def predict_product(self):
        prediction = { 
            'status': 'prediction for product completed',
            'predicted_products':[
                {'product': 'Abamectina', 'chance': '90%'},
                {'product': 'Bogard', 'chance': '70%'},
                {'product': 'lash', 'chance': '50%'}
            ]
        }
        return prediction

    def predict_dose(self):
        prediction = {
            'status': 'prediction for dose completed',
            'predicted_doses':[
                {'dose': '20cc', 'chance': '90%'},
                {'dose': '180/100', 'chance': '70%'},
                {'dose': '10cc', 'chance': '50%'}
            ]
        }
        return prediction

    def predict_machine(self):
        prediction = {
            'status': 'prediction for machine completed',
            'predicted_machines':[
                {'machine': 'pulverizadora grande', 'chance': '90%'},
                {'machine': 'mochila 20 litros', 'chance': '70%'},
                {'machine': 'pulverizadora chica', 'chance': '50%'}
            ]
        }
        return prediction

    def predict_quantity(self):
        prediction = {
            'status': 'prediction for quantity completed',
            'predicted_quantity':[
                {'quantity': '1,5', 'chance': '90%'},
                {'quantity': '3,14', 'chance': '70%'},
                {'quantity': '2,25', 'chance': '50%'}
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
                'product': 'self.product',
                'quantity': 'self.quantity',
                'dose': 'self.dose',
                'machine': 'self.machine',
            }
        }
        return prediction
    