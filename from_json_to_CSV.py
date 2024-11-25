import json
import csv

path_json = 'products.json'
path_new_csv = 'products_csv.csv'

with open(path_json, mode = 'r') as file:
    products = json.load(file)

    with open(path_new_csv, mode = 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=products[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(products)

import statistics
muestra = [1,3,5]
media= statistics.mean(muestra)
print(f'media: {media}')
mode = statistics.mode(muestra)
print(f'mode: {mode}')
stdev = statistics.stdev(muestra)
print(f'Standard dev: {stdev}')
