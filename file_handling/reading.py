# Hay tres modos para leer un archivo con la funciòn open ()

# "r"para leer
# "a" para agregar al final (append)
# "w" para sobre escribir el contenido

file = open('file_handling/sample.txt', "r", encoding="UTF-8")
# La funciòn open entrega un "objeto". Entendemos un objeto
# como algo que tiene "datos" y "metodos". Los mètodos son para
#manipular sus datos

print(file)

# Para leer el contenido del objeto file, tenemos el mètodo del objeto
#read()

print(file.read())

# Podemos leer el archivo utilizndo for
file = open('file_handling/sample.txt', "r", encoding="UTF-8")

for line in file:
    print(line)

#Luego de utilizar el archivo debemos cerrarlo
file.close()