'''
print("Ejericio 1:")

for n in range(0,101):
    if n%7 == 0 and n%13 == 0:
        print("The number "+ str(n) + " is a multiple of 7")
        print("The number "+ str(n) + " is a multiple of 13")
    elif n%7 == 0:
        print("The number "+ str(n) + " is a multiple of 7")
    elif n%13 == 0:
        print("The number "+ str(n) + " is a multiple of 13")

print("------")

print("Ejercicio 2:")

numero = int(input("Enter one number between 0 and 10: "))

if 0 < numero < 10:
    for n in range(0,11):
        print(str(numero)+"*"+str(n)+"="+str(numero * n))
else:
    print("The number is out of the boundaries")

print("------") 

print("Ejercicio 3: ")

numbers = int(input("How many numbers do you want input?"))

while numbers <=0:
    numbers = int(input("The value is not right. How many numbers do you want input?"))
    

for n in range(numbers):
    number = int(input("Enter one number greater than 0:"))
    if number > 0:
        if number%2 == 0:
            print("The number " + str(number) + " is even")
        else:
            print("The number " + str(number) + " is odd")
    else:
        print("The number is not valid, it should be greater than 0")
        number = int(input("Enter one number greater than 0:"))
        if number%2 == 0:
            print("The number " + str(number) + " is even")
        else:
            print("The number " + str(number) + " is odd")
    
print("-------")


print("Ejercicio 4:")

number = int(input("Enter one number greater than 0: "))
suma = (number*(number+1)/2)
while number <= 0:
    number = int(input("The number is not right, try again."))    
if number > 0:
    suma = (number*(number+1)/2)
    for n in range(1,number+1):
        print("The sum of the " + str(number) + " first numbers is " + str(suma))
        break    

print("------")


print("Ejercicio 5: ")
num = 1
cont = 0
while num >= 0:
    num = int(input("Enter a number(negative to finish): "))
    if num > 0:
        cont = cont + 1

print("You have entered "+ str(cont) + " positive numbers")

print("--------")


print("Ejercicio 6: ")

numberA = int(input("Enter one number: "))
numberB = int(input("Enter one number: "))

contador = 0
suma = 0
if numberB >0:
    while contador < abs(numberB):
        suma += numberA
        contador += 1
elif numberB < 0:
    while contador < abs(numberB):
        suma -= numberA
        contador += 1
print(suma)


print("--------")

print("Ejercicio 7:") 

numbers = int(input("How many numbers do you want input?"))
contador = 0

while numbers <= 0:
    numbers = int(input("How many numbers do you want input"))
    
for n in range(numbers):
    number = int(input("Enter one number greater than 0:"))
    while number <= 0:
        number = int(input("The number is not valid, it should be greater than 0"))
        contador += number
    else:
        contador += number
media = float(contador / numbers)
print("The medium is "+ str(media))

print("-------")

print("Ejercicio 8:")

number1 = int(input("Enter one number: "))
pregunta = input("Do you want to enter more number (Y/N)?")
menor = number1
while pregunta == "Y":
    number = int(input("Enter one number: "))
    if number < number1:
        menor = number
    pregunta = input("Do you want to enter more number (Y/N)?")
print("The smallest number is" + str(menor))
    
print("---------")

print("Ejercicio 9: ")

numero = int(input("Enter an integer positive number greater than 0:"))
contador = 0
while numero <0:
    numero = int(input("The number is not valid, try again: "))
    
for n in range(1,numero):
    if numero % n == 0:
        contador += n
if numero == contador:
    print("The number is perfect")
else:
    print("The number is not perfect")    
    

 
print("Ejercicio 10: ")

number = int(input("Enter an integer positive number: "))
contador = 1
while number < 0:
    number = int(input("The number is not valid, try again: "))
else:
    for n in range(1,number+1):
        contador *= n
    print("The factorial is " + str(contador))
       
        
while number < 0:
    contador = contador * number
    number -= 1   
print(contador)       
    




print("Ejercicio 17:")

num1 = int(input("Dime el numero minimo del rango: "))
num2 = int(input("Dime el numero maximo del rango: "))

for x in range(num1,num2):
    if x%2 == 0:
        print(x)

print("--------")

print("Ejercicio 18:")

num1 = int(input("Dime el minimo del rango: "))
num2 = int(input("Dime el maximo del rango: "))

while num1 > num2:
    num1 = int(input("Dime el minimo del rango: "))
    num2 = int(input("Dime el maximo del rango: "))
   
dentro = 0
fuera = 0
igual = 0

num0 = int(input("Introduce un numero: "))
while num0 != 0:
    if num1 < num0 < num2:
        dentro += num0
    elif num0 < num1 or num0 > num2:
        fuera += 1
    elif num0 == num1 or num0 == num2:
        igual += 1
        
    num0 = int(input("Introduce un numero: "))
    
print("La suma es " + str(dentro))
print("Hay "+ str(fuera)+ " fuera del intervalo")
print("Hay " + str(igual)+ " iguales que los limites")

print("--------")

print("Ejercicio 19: ")

base = int(input("Dame la base: "))
exponente = int(input("Dame el exponente: "))
cuenta = 1
contador = 0

while exponente > contador:
    cuenta *= base
    contador += 1
print(cuenta)
    
print("--------")

print("Ejercicio 20: ")

contador = 1
cuenta = 10
total = 10

while contador < 20:
    cuenta *= 2
    total += cuenta
    contador += 1
    print("En el mes " + str(contador) + " tiene que pagar " + str(cuenta))
print("El total es " + str(total))

print("--------")


print("Ejercicio 21: ")

numero = int(input("Cuantos numeros primos quieres mostrar: "))
contador = 1
num = 1

for n in range(1,numero+1):
    for i in range(1,n):
        if n%n==0 and n%1==0 and not(n%i==0):
            print(n)
        
'''


    
