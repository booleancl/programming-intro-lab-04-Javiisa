#Tenemos expresiones que se pueden evaluar en tèrminos boleanos o dicòtomicos
#Ejemplo

print(10>9)

#Esto nos permite hacer ejecuciones condicionales,por ejemplo

def is_adult(age):
    if age >= 18:
       return True
    else:
       return False

gaby_age = 33
charlotte_age = 33

#Estas siguientes intrucciones las prodriamos leer como:
#"Si el resultado es is_adult ejecutada con la variable gaby_age o paola_age
#Es verdadero,entonces el programa imprime'¿quieres una cerveza'
#DE OTRO MODO (else)imprime 'cantemos chuchuwa?'"
if is_adult(charlotte_age):
    print("¿quieres una cerveza?")
else:
    print("cantemos chuchuwa?")    

#elif es una abreviaciòn de "eslse if", nos pemite seguir evaluando expresiones.podemos tener tantos como podamos
if (charlotte_age > gaby_age):
    print("Charlotte es mayor que Gaby")
elif charlotte_age < gaby_age:
    print("Charlotte es menor que Gaby")
else:
    print("Tienen la misma edad Gaby y Charlotte")    