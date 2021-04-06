import re

class serviverde_trasformer():

    def value_for_date(self, row):    
        return row['FECHA']

    def value_for_plot(self, row): 
        return row['LOTE']

    def value_for_unit(self, row):
        return 'planta'

    def value_for_crop(self, row):
        if(row['Variedad'] == ""):
            return ""
        words = row['Variedad'].split()
        return words[0]

    def value_for_quantity(self, row):
        if (not row['CANTIDAD'].isnumeric()):
            return 50
        return row['CANTIDAD']

    def value_for_harvest_duration(self, row):
        return "7"

    def value_for_time_to_harvest(self, row):
        time_to_harvest = row['fecha de cosecha'] 
        if (time_to_harvest == ""):
            split_date = re.split('/', row['FECHA'])
            mounth = int(split_date[1]) + 3
            time_to_harvest = split_date[0] + "/" + str(mounth) + "/" + split_date[2]
        return 

    def value_for_expected_yield(self, row):
        quantity = self.value_for_quantity(row)
        return str(int(quantity)*2)

    def discard_row(self, row):
        if ((row['Variedad'] == "") or ("°" in row['Variedad']) or (not self.format_date_valid(row['FECHA'])) ):
            return True
        else:
            return False

    def format_date_valid(self, date):
        split_date = re.split('/', date)
        if (len(split_date) < 3):
            return False
        return True