class Car():
    def __init__(self, brand, model, count, price):
        self.brand  = brand
        self.model = model
        self.count  = count
        self.price = price
        self.available  = True
    
    def sell(self):
        if self.count>1:
            self.count -= 1
            print(f"Un auto modelo {self.model} de la marca {self.brand} ha sido vendido")
        elif self.count==1:
            self.available = False
            self.count -=1
            print(f"El último auto modelo {self.model} de la marca {self.brand} ha sido vendido")
        else:
            print(f"No hay autos disponibles del modelo {self.model} de la marca {self.brand}")
    
    def checkAvailability(self):
        return self.available
    
    def get_price(self):
        return self.price

class Customer:
    def __init__(self, name):
        self.name = name
        self.cars_purchased = []
    
    def buy_car(self, car):
        if car.checkAvailability():
            car.sell()
            self.cars_purchased.append(car)
        else:
            print(f"Lo sentimos, el auto {car.brand} {car.model} no está disponible")

def inquireCar(self, car):
    if car.checkAvailability():
        print(f"Actualmente contamos con {car.count} autos {car.brand} del modelo {car.model}")
    else:
        print(f"No hay disponibilidad de, {car.brand} del modelo {car.model}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customer = []
    
    def add_car(self, car):
        self.inventory.append(car)
        print(f"{car.count} auto(s) de la marca {car.brand} y modelo {car.model} han sido agregados al inventario") 
    
    def register_customer(self, customer):
        self.customer.append(customer)
        print(f"El cliente {customer.name} ha sido registrado satisfactoriamente")
    
    def show_available_cars(self):
        print("Autos disponibles: ")
        for car in self.inventory:
            if car.checkAvailability():
                print(f"Tenemos {car.count} de {car.brand} {car.model} con un valor de venta {car.price}")

#Crear instancias de autos
car1 = Car("Ford", "Edge", 2,"215000")

#Crear instancia de cliente
customer1 = Customer("Roddy Bonilla")

#Crear instacia de consecionario 

dealer = Dealership()
dealer.add_car(car1)
dealer.register_customer(customer1)

#Mostrar autos disponibles
dealer.show_available_cars()

#Compra de un auto

customer1.buy_car(car1)

#Consultar disponibilidad
dealer.show_available_cars()

#Compra de otro auto 
customer1.buy_car(car1)
#consulta de disponibilidad 
dealer.show_available_cars()

#intento de compra de un auto no disponible
customer1.buy_car(car1)