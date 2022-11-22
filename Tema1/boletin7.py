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
'''

n = int(input("Dime un numero: "))
cadena = ""
contador = 1
while contador <= 20:
    cadena += str(n)
    if contador != 20:
        cadena+= "-->"
    if n%2==0:
        n = n//2
    elif n%2==1:
        n = (3*n)+1
    contador += 1
    if n == 1:
        contador = 20
        n = 1
print(cadena)
'''
n1 = int(input("Dime un numero: "))
cadena1 = ""
contador = 1
while contador <= 20:
    cadena1 += str(n1)
    if contador != 20:
        cadena1+= "-->"
    if n1%2==0:
        n1 = n1//2
    elif n1%2==1:
        n1 = (3*n1)+1
    contador += 1
    if n1 == 1:
        contador = 20
        n1 = 1
print(cadena1)

print("------")

numero = int(input("Dime un numero: "))
num2 = int(input("Dime un numero: "))

lista = [numero]

while not (numero==1):
    if numero % 2 == 0:
        numero = numero//2
    else:
        numero = numero*3+1
        
    lista.append(numero)

print(lista)
print(len(lista))


lista2 = [num2]

while not (num2==1):
    if num2 % 2 == 0:
        num2 = num2//2
    else:
        num2 = num2*3+1
        
    lista2.append(num2)

print(lista2)
print(len(lista2))

print(len(lista)==len(lista2))
print("--"*10)

print("Ejercicio 6: ")

numero = int(input("Dime el año: "))
contador = 1
puzzle = 0
puzzleAcumulado = 0
dinero = 20
dineroacumulado=dinero+15

while contador <= numero:
    if contador == 1:
        puzzle+=1
        puzzleAcumulado+=1
    if contador%2==1 and not(contador==1):
        puzzle+=puzzleAcumulado*2
    elif contador%2==0:
        dinero+=dineroacumulado
    puzzleAcumulado=puzzle
    contador+=1
print(puzzle)
print(dinero)         

'''



