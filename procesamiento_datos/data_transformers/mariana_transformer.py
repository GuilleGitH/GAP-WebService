import re

class mariana_trasformer():

    def value_for_date(self, row):    
        return row['fecha siembra']

    def value_for_plot(self, row): 
        return row['lote (N a S y E a O)'] + " cantero " + row['Cantero']

    def value_for_unit(self, row):
        return 'planta'

    def value_for_crop(self, row):
        if(row['cultivo'] == ""):
            return ""
        words = row['cultivo'].split()
        return words[0]

    def value_for_quantity(self, row):
        if (row['cant surcos'] == ""):
            return 50
        return int(row['cant surcos']) * 50

    def value_for_harvest_duration(self, row):
        return "7"

    def value_for_time_to_harvest(self, row):
        split_date = re.split('/', row['fecha siembra'])
        mounth = int(split_date[1]) + 3; 
        return split_date[0] + "/" + str(mounth) + "/" + split_date[2]

    def value_for_expected_yield(self, row):
        quantity = self.value_for_quantity(row)
        return str(int(quantity)*2)

    def discard_row(self, row):
        if ((row['cultivo'] == "") or (row['cultivo'] == "descanso" ) or (row['fecha siembra'] == "")):
            return True
        else:
            return False