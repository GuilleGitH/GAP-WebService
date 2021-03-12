from .form import Form
from .predictors.application_form_predictor import ApplicationFormPredictor 


class ApplicationForm(Form):


    def __init__(self, date, time, plot, note, product, quantity, dose, machine):
        super().__init__(date, time, plot, note)
        self.quantity = quantity
        self.product = product
        self.dose = dose
        self.machine = machine
        self.predictor = ApplicationFormPredictor()

    def makePrediction(self, field): 
        switcher = {
            'product': self.predictor.predict_product,
            'dose': self.predictor.predict_dose,
            'machine': self.predictor.predict_machine,
            'quantity': self.predictor.predict_quantity,
            'all': self.predictor.predict_complete_form
        }
        func = switcher.get(field, lambda: "Invalid month")

        return func()
