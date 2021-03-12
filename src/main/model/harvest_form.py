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
            'all': self.predictor.predict_complete_form
        }
        func = switcher.get(field, lambda: "Invalid month")
        return func
