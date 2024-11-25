#leer un archivo línea por línea
"""with open('Cuento.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#Leer todas las líneas en una lista
"""with open('Cuento.txt', 'r') as file:
    lineas = file.readlines()
    print(lineas)"""

#Añadir texto al final
"""with open('Cuento.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")"""

#Obtener palabra más usada
""""contar = dict()
with open('Cuento.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            contar[word] = contar.get(word, 0) + 1
#print(contar)
big_count = None
big_word = None

for word, count in list(contar.items()):
    if big_count is None or count > big_count:
        big_word = word
        big_count = count
        print(count)

print(big_count, big_word)"""

#Contar las lineas del texto excluyendo los saltos de linea:
contar = 0
with open('Cuento.txt', 'r') as file:
    for lines in file:
        lines = lines.splitlines()
        print(lines)
        for line in lines:
            if len(line) > 0: 
                contar += 1
            else:
                pass 
print("La cantidad de lineas del texto sin contar los saltos de linea son:", contar)