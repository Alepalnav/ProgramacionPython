from random import randint

'''
print("Ejercicio 1: ")

listanum = []

for i in range(100):
    numero = randint(0,1000)
    listanum.append(numero)
    
def mayor(listanum):
    maxi = listanum[0]
    for x in listanum:
        if x > maxi:
            maxi = x 
    return maxi   

print(mayor(listanum))
    
def menor(listanum):
    men = listanum[0]
    for x in listanum:
        if x < men:
            men = x 
    return men

print(menor(listanum))

def suma(listanum):
    sumar = 0
    for x in listanum:
        sumar += x
    return sumar

print(suma(listanum))

def media(listanum):
    sumar = 0
    for x in listanum:
        sumar += x 
    return sumar//len(listanum)

print(media(listanum))

def cambiar(listanum):
    n = int(input("dime un numero para cambiar: "))
    numero = randint(1,100)
    listanum[numero] = n
    return listanum

print(cambiar(listanum))
       
print(listanum)

print("Ejercicio 2: ")

lista = [1,2,5,6]

a_escribir = lista[0]
a_guardar = 0

for i in range(len(lista)):
    a_guardar = lista[(i+1)%len(lista)] 
    lista[i+1] = a_escribir
    a_escribir = a_guardar
print(lista)


    



print("Ejercicio 3: ")

dia = int(input("Introduce el dia de la fecha: "))
mes = int(input("Introduce el mes de la fecha: "))
anio = int(input("Introduce el año de la fecha: "))
listames = ["enero", "febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
diames = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]

def mes_letra(mes,listames):
    for i in listames:
        mes1 = listames[mes+1]
    return mes1
    
def frase(mes_letra,dia,anio):
    mensaje = ""
    while dia>0:
        mensaje = "La fecha en formato largo es "+str(dia)+" de "+str(mes_letra)+ " de "+str(anio)
    return mensaje

print(frase(mes_letra, dia, anio))


print("Ejercicio 4: ")

def leerNumerosPar():
    lista = []
    n = int(input("Dime un numero: "))
    while n > 0:
        if n%2 == 0:
            lista.append(n)
        n = int(input("Dime un numero: "))
    mayor = lista[0]
    for i in lista:
        if i > lista[0]:
            mayor = i
    return lista, mayor

print(leerNumerosPar())


print("Ejercicio 5: ")

lista = [1,2,3,4,5]

def reverse(lista):
    n = 0
    lista2 = []
    while n < len(lista):
        n += 1
        lista2.append(lista[(len(lista))-n])
    return lista2

print(reverse(lista))


print("Ejercicio 6:")

lista = [2,3,4,5,6]

def estaOrdenada(lista):
    n = 1
    prueba = 0
    while n < len(lista):
        if lista[n] == lista[n-1]+1: 
            prueba += 1   
        n += 1
    return prueba == 4

print(estaOrdenada(lista))


print("Ejercicio 7: ")

ficha1 = [3,4]
ficha2 = [2,4]

def encajan(ficha1, ficha2):
    mensaje = "No es correcto"
    if (ficha2[0] == ficha1[0] or ficha2[1] == ficha1[0]) or (ficha2[0] == ficha1[1] or ficha2[1] == ficha1[1]):
            mensaje = "Es correcto"
    return mensaje 
        
print(encajan(ficha1, ficha2))
        
'''

print("Ejercicio 8: ")


lista = []
numero = int(input("Dime un numero: "))
while numero > 0:
    lista.append(numero)
    numero = int(input("Dime un numero: "))

def primos(lista):
    for i in lista:
        if i 

print(primos(lista))



