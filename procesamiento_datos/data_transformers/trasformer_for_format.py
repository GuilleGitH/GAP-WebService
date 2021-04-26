import csv
import requests


class trasformer():

    def tranformer_templete(self, src, dest, transformer):
        with open(src, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            # Abre el archvo destino, puede no existir y lo crea
            with open(dest, mode='w') as writecsv:
                # Headers necesarios para el writer
                fieldnames = ['date', 'hour', 'plot', 'crop', 'unit',
                              'quantity', 'time_to_harvest', 'harvest_duration', 'expected_yield']
                writer = csv.DictWriter(writecsv, fieldnames=fieldnames)
                # Escribe los headers
                writer.writeheader()
                # Escribe por cada fila presente en el csv original
                # 'plot': transformer.value_for_plot(row),
                for row in reader:
                    if (not transformer.discard_row(row)):
                        newRow = {'date': transformer.value_for_date(row),
                                  'plot': 1,
                                  'crop': transformer.value_for_crop(row),
                                  'unit': transformer.value_for_unit(row),
                                  'quantity': transformer.value_for_quantity(row),
                                  'time_to_harvest': transformer.value_for_time_to_harvest(row),
                                  'harvest_duration': transformer.value_for_harvest_duration(row),
                                  'expected_yield': transformer.value_for_expected_yield(row)}
                        writer.writerow(newRow)
                        resp = requests.post(
                            'http://127.0.0.1:5000/sowing_sql/', json=newRow)

    def merge_two_csv(self, csv1, csv2, dest):
        file1 = open(csv1, "r")
        file2 = open(csv2, "r")
        file_dest = open(dest, "w")

        for line in file1:
            file_dest.write(line)

        trap = True
        for line in file2:
            if(trap):
                trap = False
            else:
                file_dest.write(line)
