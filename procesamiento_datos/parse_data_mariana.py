import csv
import re

def time_to_harvest(date, crop):
    split_date = re.split('/', date)
    mounth = int(split_date[1]) + 3; 
    return split_date[0] + "/" + str(mounth) + "/" + split_date[2]

def proccess_variety_mariana(variety):
    if(variety == ""):
        return ""
    words = variety.split()
    return words[0]

def bad_row_treat_mariana(row):
    if ((row['cultivo'] == "") or (row['cultivo'] == "descanso" ) or (row['fecha siembra'] == "")):
        return True
    else:
        return False

def quantity(quantity):
    if (quantity == ""):
        return 50
    return int(quantity) * 50

# Abre el archivo csv fuente
with open('mariana_merge.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    # Abre el archvo destino, puede no existir y lo crea
    with open('procesado_mariana.csv', mode='w') as writecsv:
        # Headers necesarios para el writer
        fieldnames = ['date', 'hour', 'plot', 'crop', 'unit',
                      'quantity', 'time_to_harvest', 'harvest_duration']
        writer = csv.DictWriter(writecsv, fieldnames=fieldnames)
        # Escribe los headers
        writer.writeheader()
        # Escribe por cada fila presente en el csv original
        for row in reader:
            if (not bad_row_treat_mariana(row)):

                newRow = {'date': row['fecha siembra'], 'plot': row['lote (N a S y E a O)'] + " cantero " + row['Cantero'], 'unit': 'planta', 'quantity': quantity(row['cant surcos']),
                      'time_to_harvest': time_to_harvest(row['fecha siembra'], row['cultivo']), 'crop': proccess_variety_mariana(row['cultivo'])}
                writer.writerow(newRow)