class Vehicle():
    def __init__(self, brand, model, count, price):
        #Encapsulación
        self.brand  = brand
        self.model = model
        self.count  = count
        self.price = price
        self.available  = True
    
    def sell(self):
        if self.count>1:
            self.count -= 1
            print(f"Un vehiculos modelo {self.model} de la marca {self.brand} ha sido vendido")
        elif self.count==1:
            self.available = False
            self.count -=1
            print(f"El último vehiculo modelo {self.model} de la marca {self.brand} ha sido vendido")
        else:
            print(f"No hay vehiculos disponibles del modelo {self.model} de la marca {self.brand}")
    
    #Abstracción
    def check_availability(self):
        return self.available
    
    #Abstracción
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

#Herencia
class Car(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.available:
            return f"El motor del auto {self.brand} {self.model} está en marcha"
        else:
            return f"El coche {self.brand} {self.model} no está disponible"
    #Polimorfismo
    def stop_engine(self):
        if self.available:
            return f"El motor del auto {self.brand} {self.model} se ha detenido"
        else:
            return f"El auto {self.brand} {self.model} no está disponible"

#Herencia
class Bike(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.available:
            return f"La bicicleta {self.brand} {self.model} está en marcha"
        else:
            return f"La bicicleta {self.brand} {self.model} no está disponible"
    
    #Polimorfismo
    def stop_engine(self):
        if self.available:
            return f"La bicicleta {self.brand} {self.model} se ha detenido"
        else:
            return f"La bicicleta {self.brand} {self.model} no está disponible"
    
class Truck(Vehicle):
    def start_engine(self):
        if not self.available:
            return f"El motor del camión {self.brand} {self.model} está en marcha"
        else:
            return f"El camióne {self.brand} {self.model} no está disponible"
    
    def stop_engine(self):
        if self.available:
            return f"El motor del camión {self.brand} {self.model} se ha detenido"
        else:
            return f"El camión {self.brand} {self.model} no está disponible"
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.vehicles_purchased = []
    
    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            vehicle.sell()
            self.vehicles_purchased.append(vehicle)
        else:
            print(f"Lo sentimos, el auto {vehicle.brand} {vehicle.model} no está disponible")
    
    def inquireVehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            print(f"Actualmente contamos con {vehicle.count} de la marca {vehicle.brand} del modelo {vehicle.model} y tiene un valor de venta de {vehicle.price}")
        else:
            print(f"No hay disponibilidad de, {vehicle.brand} del modelo {vehicle.model}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"{vehicle.count} de vehiculo(s) {vehicle.brand} {vehicle.model} han sido añadidos al inventario")
    
    def show_available_vehicles(self):
        for vehicle in self.inventory:
            if vehicle.check_availability():
                print(f"Tenemos {vehicle.count} disponible de {vehicle.brand} {vehicle.model} por {vehicle.get_price()}")
            else:
                print(f"No tenemos disponibilidad del vehiculo {vehicle.brand} {vehicle.model}")

#Crear instancias de autos
car1 = Car("Ford", "Edge", 2, 30000)

#Crear instancia Bike
bike1 = Bike("Yamaha", "XT600", 5, 20000)

#Crear instancia de truck
truck1 = Truck("Volvo", "FH16", 1, 80000)

#Crear instancia de cliente
customer1 = Customer("Roddy Bonilla")

#Crear instancia de tienda

dealership= Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#Mostrar Vehicle

dealership.show_available_vehicles()

#Cliente consulta un vehicle
customer1.inquireVehicle(bike1)

#cliente compra bike

customer1.buy_vehicle(bike1)

#Mostrar disponibilidad
dealership.show_available_vehicles()