import csv

file_path = 'products.csv'
updated_file_path  = 'products_updated3.csv'

with open(file_path, mode = 'r') as file:
    csv_reader = csv.DictReader(file)
    #obtener los nombre de las columns
    fieldnames = csv_reader.fieldnames + ['total_value'] + ['low_inventory']

    with open(updated_file_path, mode = 'w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader() #escribimos los encabezados

        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            if int(row['quantity']) < 50:
                row['low_inventory'] = str('Must be purchased')
                csv_writer.writerow(row)
            else:
                row['low_inventory'] = str('Not yet purchased')
                csv_writer.writerow(row)
        
