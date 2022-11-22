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
