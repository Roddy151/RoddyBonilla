from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:
    #Crear un diccionario con valor por defecto 0
    product_count = defaultdict(int)
    print(product_count)
    for product in orders:
        product_count[product] +=1
        print(product_count)
    return product_count
orders = ['Laptop', 'Smarphone','Laptop', 'Tablet', 'Tablet', 'Iphone']
count = count_products(orders)
print(count)