from .form_predictor import FormPredictor

class HarvestFormPredictor(FormPredictor):

    def predict_quantity_kg(self):
        prediction = {
            'status': 'prediction for quantity completed',
            'predicted_quantities':[
                {'quantity': '200', 'chance': '90%'},
                {'quantity': '350', 'chance': '70%'},
                {'quantity': '180', 'chance': '50%'}
            ]
        }
        return prediction

    def predict_quantity_other_unit(self):
        prediction = {
            'status': 'prediction for quantity other unit completed',
            'predicted_quantities_other_units':[
                {'harvest_quantity': '2', 'chance': '90%'},
                {'harvest_quantity': '3', 'chance': '70%'},
                {'harvest_quantity': '10', 'chance': '50%'}
            ]
        }
        return prediction