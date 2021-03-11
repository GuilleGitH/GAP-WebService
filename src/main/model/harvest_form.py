from .form import Form


class HarvestForm(Form):
    def __init__(self, date, time, plot, note, quantity, harvest_quantity):
        super().__init__(date, time, plot, note)
        self.quantity = quantity
        self.harvest_quantity = harvest_quantity
