#podemos crear o definir nuestras podrias funciones 
#Lo hacemos con la palabra especial "def"y el cuerpo
#la funcion debe ir correctamente indectado

def chuchuwa(inst):
    print("Chuchuwa chuchuwa chuchuwa wa wa!")
    print("Chuchuwa chuchuwa chuchuwa wa wa!")
    print("Atenciòn!, Compañìa")
    print(inst)

print(chuchuwa)
print(type(chuchuwa))

#El llamado de la funciòn
chuchuwa("Mano hacia el frente")
chuchuwa("hombro hacia atràs")
#Las funciones deben llamarse o ejecutarse con los mismos parametros que se definio.
result = chuchuwa("Lengua afuera")
#Si la funcion no tiene un valor de retorno nos entregara "none" que es para representar"Nada"
print(result)
