day = 22
month = 11
year = 2022
list = [day,month,year]
def getDayOfWeek(list):
    date = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    a = (14-month)//12
    y = year-a
    m = month + 12 * a - 2
    d = (day + y + y/4 - y/100 + y/400 + (31*m)/12)%7
    return date[int(d)]
    
print(getDayOfWeek(list))
