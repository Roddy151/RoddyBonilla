def divide(a: int, b:int) -> float:
    #Validar que ambos parametros sean enteros 
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Ambos parámetros deben ser enteros')
    
    #Verificamos que el divisor no sea cero
    if b==0:
        raise ValueError('El divisor no puede ser cero.')
    
    return a/b
#res_1 = divide(10, '2')
#res_2 = divide(10,0)
res_3 = divide(10,2)
print(res_3)