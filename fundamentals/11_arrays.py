# Los arreglos (listas) son una ESTRUCTURA DE DATOS FUNDAMENTALES
#que permite agrupar valores, separados por coma

first_array = ['sacar la basura','peinarse','dormir','secar la ropa']

#En python el primer elemento de un arreglo tiene posiciòn (indice) 0
print(first_array[0])
print(first_array[1])
print(first_array[2])
print(first_array[3])

#No existe el elemento con indice 4 y python da un error
# print(first_array[4])

#podemos saber el largo de un arreglo o lista con la funciòn pre definida len()
print(len(first_array))

#ademas,podemos agregar elementos al final de arreglo con el mètodo append
first_array.append('Comer')
first_array.append('Dormir')

#podemos indicar la posiciòn del nuevo elemeto a agregar con insert
first_array.insert(0,'Levantarse')

#Podemos imprimir la lista completa
print(first_array)
