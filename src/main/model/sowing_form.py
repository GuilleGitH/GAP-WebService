from .form import Form


class SowingForm(Form):
    def __init__(self, date, time, plot, note, crop, quantity, time_to_harvest, harvest_duration, expected_yield):
        super().__init__(date, time, plot, note)
        self.crop = crop
        self.quantity = quantity
        self.time_to_harvest = time_to_harvest
        self.harvest_duration = harvest_duration
        self.expected_yield = expected_yield
