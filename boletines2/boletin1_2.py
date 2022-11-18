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

lista = ["hola",2,3,4,5]

def reverse(lista):
    n = 0
    lista2 = []
    while n < len(lista):
        n += 1
        lista2.append(lista[(len(lista))-n])
    return lista2

print(reverse(lista))


print("Ejercicio 6:")

lista = [2,3,7,9,15]

def estaOrdenada(lista):
    n = 1
    prueba = 0
    while n < len(lista):
        if lista[n] > lista[n-1]: 
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
        




print("Ejercicio 8: ")


lista = []
numero = int(input("Dime un numero: "))
while numero > 0:
    lista.append(numero)
    numero = int(input("Dime un numero: "))
def numero_primos(n):
    es_primo = True
    for i in range(2,n):
        if n%i == 0:
            es_primo = False
    return es_primo

primos = []
for elemento in lista:
    if numero_primos(elemento):
        primos.append(elemento)

print(primos)

def sumatorio(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

print(sumatorio(lista))

def promedio(lista):
    suma = 0
    for i in lista:
        suma += i 
    media = suma//len(lista)
    return media

print(promedio(lista))
def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i
    return fac

listaFactorial = []
for elemento in lista:
    listaFactorial.append(factorial(elemento))
    
print(listaFactorial)


print("Ejercicio 9: ")

lista = [1,4,2,5,6]
k = 5

def menores(lista,k):
    menor = []
    for i in lista:
        if i < k:
            menor.append(i)
    return menor

print(menores(lista, k))
            
def mayores(lista,k):
    mayor = []
    for i in lista:
        if i > k:
            mayor.append(i)
    return mayor

print(mayores(lista, k))

def multiplos(lista,k):
    multiplo = []
    for i in lista:
        if i%k == 0:
            multiplo.append(i)
    return multiplo

print(multiplos(lista, k))
'''
print("Ejercicio 10: ")

numero = "101101B"

def conversor(numero):
    lista2 = []
    if numero[-1] == "B":
        numero = numero[0:len(numero)-1]
        for i in numero:
            if int(i) > 1:
                assert Exception("Los numeros binarios no son mayores que 1")
        n = 0
        for n in numero:
            lista2.append(n)
        x = 0
        y = len(lista2)-1
        producto = 0
        while x < len(lista2):
            producto += int(lista2[x]) * (2 ** y)
            x += 1
            y -= 1
        return producto
    if numero[-1] == "D":
        numero = numero[0:len(numero)-1]
        for i in numero:
            if not (0<=int(i)<9):
                assert Exception("La base decimal debe ser entre 0 y 9")
        numero = int(numero)
        binario = 0
        multiplicador = 1
        while numero != 0:
            binario += numero % 2 * multiplicador
            numero //= 2
            multiplicador *= 10
        return binario
print(conversor(numero))
'''
print("Ejercicio 11: ")

lista1 = [1,4,5,6]
lista2 = [4,5,7,1,1]

def intersect(lista1,lista2):
    lista3 = []
    for i in lista1:
        if i in lista2:
            lista3.append(i) 
    return lista3

print(intersect(lista1, lista2))

print("Ejercicio 12: ")

lista1 = [1,3,4,6]
lista2 = [1,2,4,7]

def unionLista(lista1,lista2):
    lista3 = []
    for i in lista2:
        lista3.append(i)
    for i in lista1:
        if i not in lista2:
            lista3.append(i)
    lista3.sort()
    return lista3

print(unionLista(lista1, lista2))

            
print("Ejercicio 13: ")

listaNombres = ["Alejandro", "Alvaro", "Paco"]
letra = "A"

def nombresLetra(listaNombres, letra):
    lista3 = []
    for i in listaNombres:
        if letra == i[0]:
            lista3.append(i)
    return lista3

print(nombresLetra(listaNombres, letra))
        


print("Ejercicio 14: ")

lista = ["hola", "ordenador", "mundo","hxla", "ordenados"]

def compararLista(lista):
    elemento = lista[0]
    mayor = []
    for i in lista:
        if len(i) == len(elemento):
            palabra1 = []
            palabra2 = []
            cantidad1 = []
            cantidad2 = []
            for x in i:
                if x in palabra1:
                    cantidad1.append(x)
                palabra1.append(x)
            for y in elemento:
                if y in palabra2:
                    cantidad2.append(y)
                palabra2.append(y)
            if len(cantidad1) > len(cantidad2):
                mayor = [i] 
            elif len(cantidad2) > len(cantidad1):
                mayor = [elemento]                      
        if len(i) > len(elemento):
            elemento = i
            mayor = [i]
    return mayor

print(compararLista(lista))

'''
