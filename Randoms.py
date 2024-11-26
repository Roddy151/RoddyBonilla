import random

#Generar un numero entero aleatorio

x_random = random.randint(1,10)
print(x_random)

#Elegir colores aleatorios

colors = ['Red', 'Blue', 'Green']
random_color = random.choice(colors)
print(random_color)

#Barajar una lista de cartas
cards = ['As', 'King', 'Queen', 'J', '10']
random.shuffle(cards)
print(cards)