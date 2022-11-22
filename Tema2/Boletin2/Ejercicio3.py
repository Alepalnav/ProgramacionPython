dias = [31,28,31,30,31,30,31,31,30,31,30,31]
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio","julio","agosto","septiembre", "octubre", "noviembre", "diciembre"]
month = "febrero"
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