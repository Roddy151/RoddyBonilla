import os 

#Get the current work directory
cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)

#List files of the current work directory
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Los Archivos txt: ", txt_files)

os.rename('Cuento.txt', 'caperucita.txt')
print("El archivo renombrado: ")

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Los Archivos txt: ", txt_files)