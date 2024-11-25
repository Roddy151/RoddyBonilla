import json

file_path = 'products.json'

new_product = {
    "name": 'Headphones',
    "price": 1900,
    "quantity": 75,
    "brand": 'PlayStation',
    "category": 'Accessories',
    "entry_date": '2024-11-24'
}

with open(file_path, mode = 'r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, mode = 'w') as file:
    json.dump(products, file, indent=4)
