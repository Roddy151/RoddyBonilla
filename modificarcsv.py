import csv

new_product = {
    'name': "Wireless charger",
    'prece': 75,
    'quantity': 100,
    'brand': "PhonePro",
    'category': "Accessories",
    'entry_date': "2024-11-23"
}

with open('products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)
