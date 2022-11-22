
print("Ejercicio 2: ")

fecha=input("Introduzca una fecha en formato dd-mm-yyyy: ")
hemisferio = input("Introduzca el hemisferio (Norte/sur)")

day = int(fecha[0:2])
month = int(fecha[3:5])
year = int(fecha[6:10])

if (month==10 or month==11) or (23<=day<=31 and month==9) or (month==12 and 1<=day<=21):
    print("Es otoño")