from .form import Form
from .predictors.harvest_form_predictor import HarvestFormPredictor 

class HarvestForm(Form):
    def __init__(self, date, time, plot, note, quantity, harvest_quantity):
        super().__init__(date, time, plot, note)
        self.quantity = quantity
        self.harvest_quantity = harvest_quantity
        self.predictor = HarvestFormPredictor()

    def makePrediction(self, field):

        switcher = {
            'type': self.predictor.predict_quantity_kg,
            'quantity_other_unit': self.predictor.predict_quantity_other_unit,

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
                'quantity': 'self.quantity',
                'harvest_quantity': 'self.harvest_quantity',
            }
        }
        return func
