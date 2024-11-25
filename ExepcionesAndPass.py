try:
    divisor=int(input("Ingresar un numero divisor: "))
    result=100/divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser cero")
    print("Ha ocurrido un error: ", e)
except ValueError as e:
    print("Debes introducir un numero valido")
    print("Ha ocurrido un error: ", e)