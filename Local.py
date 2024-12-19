x = 100

def local_funtion():
    x = 10 #Variable local
    print(f'El valor de la variable {x}')

def show_global():
    print(f'El valor de la variable es {x}')

local_funtion()
show_global()

print(x) 
