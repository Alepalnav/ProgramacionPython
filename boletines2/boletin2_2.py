
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

print("Ejercicio 3: ")

dias = [31,28,31,30,31,30,31,31,30,31,30,31]
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio","julio","agosto","septiembre", "octubre", "noviembre", "diciembre"]
month = "marzo"
year = "2020"

def computeDaysInMonth(month, year, meses, dias):
    for n in range(len(dias)):
        dias[n] = meses[n]
    return dias

print(computeDaysInMonth(month, year, meses, dias))


