
print("Bievenido al programa")
user_input =""

while user_input != "exit":
    print("##################")
    print("ingresa una opciòn")
    print("1", "agrega contenido")
    print("2", "leer contenido")
    print("exit", "para salir")
    print("###################")

    user_input = input()

    if user_input == "1":
        file =open("file_handling/demo_two.txt","a")
        user_content = input("Ingresa el contenido\n")
        file.write(user_content + "\n")
        file.close()
    elif user_input == "2":
        file = open("file_handling/demo_two.txt","r")    
        for line in file:
            print(line)
    else:
         print("opciòn incorrecta")        
print ("Chu chau")    