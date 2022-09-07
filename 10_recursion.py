import time

# Es perfectamente posible llamar una funciòn de otra
# Lo hicimos cuando calculamos el volumen de un cilindro.

# Pero tambièn es perfectamnte posible que una funciòn se llame a si misma
# Esto es una tècnica muy poderosa para ciertos problemas

#funciòn conteo regresivo
#Es una funciòn que se llama a si misma
def countdown(number):
    if number <= 0:
        print("KABUMM")
    else:
        print(number)
        time.sleep(0.5)
        countdown(number - 1)

countdown(5)

def super_sum(number):
    if number <= 0:
        return number
    else:
        return number + super_sum(number - 1)
print(super_sum(3))
