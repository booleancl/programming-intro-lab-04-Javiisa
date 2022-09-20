# Similar a los arreglos,los diccionarios nos permiten
# escructurar informaciòn,Con la diferencia de que los
# elementos estàn ordenados por llave y no por ìndice.Ejemplo

my_car = {
    "brand": "Mazda",
    "model": "5",
    "year": 2022,
    "options":["5 puertas", "Aire acondicionado", "Frenos ABS"],
    "available": True
} 

print(my_car["brand"])
print(my_car["year"])
print(my_car["options"])

# Si queremos todas las llaves, tenemos el mètodo. keys()
print(my_car.keys())
# Si queremos todos los valores, tenemos el mètodo .values()
print(my_car.values())

#podemos tambien actualizar valores de una determinada llave

my_car["model"] = "9"
print(my_car["model"])

# Tambièn podemos agregar llaves y valores
my_car["color"] = "silver"
print(my_car)