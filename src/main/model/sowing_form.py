from .form import Form
from .predictors.sowing_form_predictor import SowingFormPredictor 

class SowingForm(Form):
    def __init__(self, date, time, plot, note, crop, quantity, time_to_harvest, harvest_duration, expected_yield):
        super().__init__(date, time, plot, note)
        self.crop = crop
        self.quantity = quantity
        self.time_to_harvest = time_to_harvest
        self.harvest_duration = harvest_duration
        self.expected_yield = expected_yield
        self.predictor = SowingFormPredictor()

    def makePrediction(self, field):
        switcher = {
            'crop': self.predictor.predict_crop,
            'quantity': self.predictor.predict_quantity,
            'time_to_harvest': self.predictor.predict_time_to_harvest,
            'harvest_duration': self.predictor.predict_harvest_duration,
            'expected_yield': self.predictor.predict_expected_yield,
            'all': self.predictor.predict_complete_form
        }
        func = switcher.get(field, lambda: "Invalid month")
        return func(form=self)
