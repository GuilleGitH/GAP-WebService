from .form import Form


class HarvestForm(Form):
    def __init__(self, date, time, plot, note, quantity, harvest_quantity):
        super().__init__(date, time, plot, note)
        self.quantity = quantity
        self.harvest_quantity = harvest_quantity

    def makePrediction():
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
        return response
