x = 5

def modify_global():
    global x
    x += 3
    print(f'El valor modificado es {x}')

modify_global()
print(x)