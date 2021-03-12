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
                'crop': 'self.crop',
                'quantity': 'self.quantity',
                'time_to_harvest': 'self.time_to_harvest',
                'harvest_duration': 'self.harvest_duration',
                'expected_yield': 'self.expected_yield',
            } 
        }
        return func()
