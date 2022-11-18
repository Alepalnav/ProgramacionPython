'''
Created on 31 oct. 2022

@author: Ale Palma
'''
print("#######################")
print("# Bienvenido al IES Jacarandá!!: ")
print("  1. Alumnos que ha entrado: ")
print("  2. Alumnos que han abandonado el centro: ")
print("  3. Alumnos en el IES: ")
print("  4. Salir ")
print("#######################")
opcion = int(input(" "))
personas = 0

while opcion > 4 or opcion < 1:
    opcion = int(input("El numero debe ser de 1 a 4: "))
    
while 3 >= opcion >= 1:
    if opcion == 1:
        numero = int(input("Cuantas personas entran: "))
        personas += numero
    elif opcion == 2:
        numero = int(input("Cuantas personas salen: "))
        while numero > personas:
            numero = int(input("No pueden salir mas personas de las que hay en el centro, vuelve a introducir el dato: "))
        personas -= numero
    elif opcion == 3:
        print("Hay "+ str(personas)+" alumnos en el centro. ")
    print("#######################")
    print("# Bienvenido al IES Jacarandá!!: ")
    print("  1. Alumnos que ha entrado: ")
    print("  2. Alumnos que han abandonado el centro: ")
    print("  3. Alumnos en el IES: ")
    print("  4. Salir ")
    print("#######################")
    opcion = int(input(" "))
    while opcion > 4 or opcion < 1:
        opcion = int(input("El numero debe ser de 1 a 4: "))


