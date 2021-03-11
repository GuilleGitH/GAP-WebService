from .form import Form


class ApplicationForm(Form):
    def __init__(self, date, time, plot, note, product, quantity, dose, machine):
        super().__init__(date, time, plot, note)
        self.quantity = quantity
        self.product = product
        self.dose = dose
        self.machine = machine

    def makePrediction():
        response = {
            'status': 'prediction completed',
            'predicted_form': {
                'date': 'self.date',
                'time': 'self.time',
                'plot': 'self.plot',
                'note': 'self.note',
                'product': 'self.product',
                'quantity': 'self.quantity',
                'dose': 'self.dose',
                'machine': 'self.machine',
            }
        }

        return response
