def outer_funtion():
    x = 'enclosing'
    def inner_funtion():
        nonlocal x
        x = 'modified'
        print(f'El valor en inner es {x}')
    inner_funtion()
    print(f'El valor outer es {x}')
outer_funtion()