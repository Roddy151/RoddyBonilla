from collections import Counter

def count_sales(orders: list[str]) -> Counter:
    #Usar Counter para contar los productos de cada tipo hay en la lista
    return Counter(orders)
orders = ['Laptop', 'Smarphone','Laptop', 'Tablet', 'Tablet', 'Iphone']
result = count_sales(orders)
print(result)
