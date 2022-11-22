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
