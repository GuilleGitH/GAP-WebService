from .form_predictor import FormPredictor

class SowingFormPredictor(FormPredictor):
    def predict_crop(self):
        prediction = {
            'status': 'prediction for crop completed',
            'predicted_crops':[
                {'crop': 'Tomate', 'chance': '90%'},
                {'crop': 'Lechuga', 'chance': '70%'},
                {'crop': 'zuccini', 'chance': '50%'}
            ]
        }
        return prediction

    def predict_quantity(self):
        prediction = {
            'status': 'prediction for quantity completed',
            'predicted_quantities':[
                {'quantity': '200', 'chance': '90%'},
                {'quantity': '100', 'chance': '70%'},
                {'quantity': '50', 'chance': '50%'}
            ]
        }
        return prediction

    def predict_harvest_duration(self):
        prediction = {
            'status': 'prediction for harvest_duration completed',
            'predicted_harvest_durations':[
                {'harvest_duration': '7', 'chance': '90%'},
                {'harvest_duration': '3', 'chance': '70%'},
                {'harvest_duration': '9', 'chance': '50%'}
            ]
        }
        return prediction

    def predict_time_to_harvest(self):
        prediction = {
            'status': 'prediction for time_to_harvest completed',
            'predicted_time_to_harvests':[
                {'time_to_harvest': '30', 'chance': '90%'},
                {'time_to_harvest': '45', 'chance': '70%'},
                {'time_to_harvest': '60', 'chance': '50%'}
            ]
        }
        return prediction

    def predict_expected_yield(self):
        prediction = {
            'status': 'prediction for expected_yield completed',
            'predicted_expected_yields':[
                {'expected_yield': '100', 'chance': '90%'},
                {'expected_yield': '300', 'chance': '70%'},
                {'expected_yield': '75', 'chance': '50%'}
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
                'crop': 'self.crop',
                'quantity': 'self.quantity',
                'time_to_harvest': 'self.time_to_harvest',
                'harvest_duration': 'self.harvest_duration',
                'expected_yield': 'self.expected_yield',
            } 
        }
        return prediction