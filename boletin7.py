'''

print("Ejercicio 1:")

num1 = int(input("Introduzca un numero: "))
num2 = int(input("Introduzca otro numero: "))

cociente = 0
resta = 0

if num1 > num2:
    resta = num1
    while resta >= num2:
        resta -= num2
        cociente += 1
    print("El cociente es " + str(cociente))    
    print("El resto es " + str(resta))
elif num2 > num1:
    resta = num2
    while resta >= num1:
        resta -= num1
        cociente += 1
    print("El cociente es " + str(cociente))    
    print("El resto es " + str(resta))
else:
    print("El cociente es 1")
    print("El resto es 0")
        
print("--------")

print("Ejercicio 2: ")

num1 = int(input("Introduzca un numero: "))
num2 = int(input("Introduzca otro numero menor: "))

cadena = ""

contador = 0

while contador < 10:
    num1 += 1
    if num1%num2 == 0:
        contador += 1
        if contador!=10:
            cadena += str(num1)+ ", "
        else:
            cadena += str(num1)

print(cadena)

print("-------")

print("Ejercicio 3: ")

num = int(input("Introduzca un numero: "))
cuadrado = num * num
while num != 0:
    cuadrado = num * num
    if num%2 == 0:
        if num<0:
            print("es par, negativo y su cuadrado es "+ str(cuadrado))
        elif num>0:
            print("es par, positivo y su cuadrado es "+ str(cuadrado))
    else:
        if num<0:
            print("es impar, negativo y su cuadrado e<s "+ str(cuadrado))
        elif num>0:
            print("es impar, positivo y su cuadrado es "+ str(cuadrado))
        
    num = int(input("Introduzca un numero: "))

print("-------")

print("Ejercicio 4: ")

num = int(input("Dime un tamaño de secuencia: "))

numero = 1
contador = 1
cadena = ""
while contador <= num:
    if contador == num:
        cadena += str(numero)
    else:
        cadena += str(numero)+","
    numero *= -5
    contador += 1
print(cadena)
    
numero=0
contador=0
cadena = ""
while contador < num:
    if contador%3==0:
        numero = 1
    elif contador%3 == 1:
        numero = -1
    elif contador%3 == 2:
        numero = 0
        
    if contador != (num-1):
        cadena += str(numero)+","
    else:
        cadena += str(numero)
    contador += 1
print(cadena)

cadena = ""
numero = 1
contador = 1
while contador <= num:
    if contador == num:
        cadena += str(numero)
    else:
        cadena += str(numero)+","
    numero *= 3
    contador += 1
print(cadena)

print("-----")
'''
print("Ejercicio 5: ")

n = int(input("Dime un numero: "))
cadena = ""
contador = 1
while contador <= 10:
    cadena += str(n)
    if contador != 10:
        cadena+= "-->"
    if n%2==0:
        n = n//2
    elif n%2==1:
        n = (3*n)+1
    contador += 1
    if n == 1:
        contador = 10
        n = 1
print(cadena)

print("------")

print("Ejercicio 6: ")




