#Las funciones pueden hacer cosas y tambn pueden retornan valores

def circle_area(radius):
    area = 3.1415*radius**2
    return area

    #En este caso la funciòn me entrega o devuelve un valor

result =circle_area(4)
print(result)

def circle_volume(radius,height):
    volume = circle_area(*radius)*height
    return volume

result_two = circle_volume(4,10)
print(result_two)