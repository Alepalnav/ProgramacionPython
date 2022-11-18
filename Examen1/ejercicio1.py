'''
Created on 31 oct. 2022

@author: Ale Palma
'''

print("Ejercicio 1: ")

eleccion1 = input("Dime tu primera eleccion: ")

while not(eleccion1 == "lagarto" or eleccion1 == "piedra" or eleccion1 == "papel" or eleccion1 == "tijera" or eleccion1 == "spock"):
    eleccion1 = input("Tu primera eleccion debe ser piedra, papel, tijera, lagarto o spock: ")
    
eleccion2 = input("Dime tu segunda eleccion: ")

while not(eleccion2 == "lagarto" or eleccion2 == "piedra" or eleccion2 == "papel" or eleccion2 == "tijera" or eleccion2 == "spock"):
    eleccion2 = input("Tu segunda eleccion debe ser piedra, papel, tijera, lagarto o spock: ")
    
if eleccion1 == eleccion2:
    print("Empatan")
elif eleccion1 == "piedra" and (eleccion2 == "tijera" or eleccion2 == "lagarto"):
    print(str(eleccion1) +" gana a "+ str(eleccion2))
elif eleccion1 == "papel" and (eleccion2 == "piedra" or eleccion2 == "spock"):
    print(str(eleccion1) +" gana a "+ str(eleccion2)) 
elif eleccion1 == "tijera" and(eleccion2 == "lagarto" or eleccion2 == "papel"):
    print(str(eleccion1) +" gana a "+ str(eleccion2))
elif eleccion1 == "lagarto" and (eleccion2 == "spock" or eleccion2 == "papel"):
    print(str(eleccion1) +" gana a "+ str(eleccion2))
elif eleccion1 == "spock" and (eleccion2 == "tijera" or eleccion2 == "piedra"):
    print(str(eleccion1) +" gana a "+ str(eleccion2))
else: 
    print(str(eleccion1) + " pierde ante "+ str(eleccion2))  
