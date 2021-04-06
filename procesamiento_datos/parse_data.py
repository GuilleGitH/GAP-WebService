import csv

# Abre el archivo csv fuente
with open('lote1_serviverde.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    # Abre el archvo destino, puede no existir y lo crea
    with open('sowing_template.csv', mode='w') as writecsv:
        # Headers necesarios para el writer
        fieldnames = ['date', 'hour', 'plot', 'crop', 'unit',
                      'quantity', 'time_to_harvest', 'harvest_duration']
        writer = csv.DictWriter(writecsv, fieldnames=fieldnames)
        # Escribe los headers
        writer.writeheader()
        # Escribe por cada fila presente en el csv original
        for row in reader:
            newRow = {'date': row['FECHA'], 'plot': '1', 'quantity': row['CANTIDAD'],
                      'time_to_harvest': row['fecha de cosecha'], 'crop': row['Variedad']}
            writer.writerow(newRow)
