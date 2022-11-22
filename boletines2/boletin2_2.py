
'''
print("Ejercicio 1: ")

n = 5

def computeFactorial(n):
    if n > 0:
        suma = 1
        for i in range(1, n + 1):
            suma *= i
        return suma
    else:
        return None
    
print(computeFactorial(n))



print("Ejercicio 2: ")

year = 2020

def isLeapYear(year):
    leapYear = True
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leapYear = True
            else: 
                leapYear = False
        else: 
            leapYear = True
    else:
        leapYear = False
    return leapYear

print(isLeapYear(year))

'''
print("Ejercicio 3: ") #preguntar

dias = [31,28,31,30,31,30,31,31,30,31,30,31]
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio","julio","agosto","septiembre", "octubre", "noviembre", "diciembre"]
month = "febrer"
year = 2020


def computeDaysInMonth(month, year, meses, dias):
    if (month not in meses) or (type(year) != int):
        return -1
    leapYear = True
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leapYear = True
            else: 
                leapYear = False
        else: 
            leapYear = True
    else:
        leapYear = False
    if leapYear == True:
        dias[1] = 29
    for n in range(len(meses)):
        if meses[n] == month:
            return dias[n]

print(computeDaysInMonth(month, year, meses, dias))

'''

print("Ejercicio 4: ") #preguntar

day = 22
month = 11
year = 2022
list = [day,month,year]
def getDayOfWeek(list):
    date = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    a = (14-month)/12
    y = year-a
    m = month + 12 * a - 2
    d = (day + y + y/4 - y/100 + y/400 + (31*m)/12)%7
    return date[int(d)]
    
print(getDayOfWeek(list))


print("Ejercicio 5: ")

num1 = 2
num2 = 3

def powerIt(num1,num2):
    if type(num2) != int:
        return num1**0
    else:
        numero =  num1**num2
        return numero

print(powerIt(num1, num2))


print("Ejercicio 6: ") #preguntar

num = -55
numeros = ["0","1","2", "3", "4","5","6","7","8","9"]
def getNumberOfDigits(num, numeros):
    num1 = str(num)
    digitos = 0
    for i in num1:
        if i in numeros :
            digitos += 1
        else:
            pass
    return digitos

print(getNumberOfDigits(num, numeros))


print("Ejercicio 7: ")

num = 7

def isPrime(num):
    contador = 0
    if (type(num) == int) > 0:
        for i in range(1,num+1):
            if num%i == 0:
                contador += 1
        return contador == 2
    else:
        return None

print(isPrime(num))

print("Ejercicio 8: ")
from math import sqrt

a = 1
b = 4
c = 3

def solveSecondOrderEquation(a,b,c):
    if not(((b**2)-4*a*c) > 0):
        return None
    else:
        x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)  
        x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)  
        print("Las soluciones de la ecuación son:")
    return x1,x2

print(solveSecondOrderEquation(a, b, c))


print("Ejercicio 9: ")

number = 50

def getPrimeDivisors(number):
    if type(number) != int:
        return None
    else:
        numeros = []
        for i in range(1,number+1):
            contador = 0
            for x in range(1,i+1):
                if i%x == 0:
                    contador += 1
            if contador == 2:
                numeros.append(i)
    return numeros

print(getPrimeDivisors(number))


print("Ejercicio 10: ")

num1 = 220
num2 = 284

def isFriendNumber(num1,num2):
    suma1 = 0
    suma2 = 0
    for i in range(1,num1+1):
        if num1%i == 0:
            suma1 += i
    for x in range(1,num2+1):
        if num2%x == 0:
            suma2 += x
    return suma1 == suma2

print(isFriendNumber(num1,num2))

'''






















