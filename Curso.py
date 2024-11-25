#Matrix
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print(matrix)
print(matrix[2][2])
#Tuple: A tuple is a built-in date type that allows you to create immutable sequences on values.  
numbers=(1,2,3,4,5)
print(numbers)
print(type(numbers))
print(numbers[1])
#Dictionary
numbers={1:"Uno", 2:"Dos", 3:"Tres"}
print(numbers)
information={"Name": "Roddy",
            "Surname": "Bonilla",
            "Age": 42}
print(information)
del information["Age"]
print(information)
key=information.keys()
print(key)
value=information.values()
print(value)
print(type(key))
print(type(value))

contacts={"Anlly":{"Name": "Anlly Matiliana", "Surnames": "Cárdenas Montilva", "Age": 42},
         "Ani":{"Name": "Anissa", "Surnames":"Bonilla Cárdenas"}}
print(contacts)
contactsKey1=contacts.keys()
contactsValue1=contacts.values()
print(contactsKey1)
print(contactsValue1)

# Configuración de una aplicación
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}
print("\n Configuración:", config)
# Contador de palabras
palabras = ["manzana", "banana", "naranja", "manzana", "banana", "banana"]
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("\n Contador de palabras:", contador)

# Mapeo de usuarios a datos
usuarios = {
    "user123": {"nombre": "Juan", "edad": 30},
    "user456": {"nombre": "Ana", "edad": 25}
}

#Lists are used to store multiple items in a single variable

squares=[x**2 for x in range(1,11)]
print("\n Squares: ", squares)

celsius = [0, 10, 20, 30, 40]
Fahrenheit = [(temp * 9/5)* 32 for temp in celsius]
print("\n Fahrenheit Temp: ", Fahrenheit )

evens = [x for x in range(1,21) if x%2==0 ]
print("\n",evens)

matrix1=[[1,2,3],
        [4,5,6],
        [7,8,9]]

transposed = [[row[i] for row in matrix1] for i in range(len(matrix1[0]))]
print("\n", matrix1)
print("\n", transposed)

#Loop and iteration controls

listNumbers=[1,2,3,4,5,6]
for i in listNumbers:
    print("\n Aquí i es igual a:", i)

for i in range(10):
    print(i)
fruits=["Orange", "Tomato", "Grape", "Pear", "Apple"]
for fruit in fruits:
    print(fruit)
    if fruit=="Orange":
        print("Orange found")

x=0
while x<5:
    if x==3:
        break
    print(x)
    x+=1

