x = 'global' #Variable global

#Función Externa
def outer_funtion():
    x = 'enclosing'
    #Función interna
    def inner_funtion():
        x = 'local'
        print (x)
    inner_funtion()
    print(x)
outer_funtion()
print(x)
