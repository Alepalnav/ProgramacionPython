print("Bienvenido al gimnasio Jacafitness")
dia1 = input("¿Que dia de la semana es?: ")
dia = dia1.upper()
horas = input("¿Que hora es?: ")
hora = int(horas[0:2])

if dia == "LUNES" or dia == "MIERCOLES" or dia == "VIERNES":
    if 12 <= hora < 14:
        print("Hay clase de spinning")
    elif 16 <= hora < 20:
        print("Hay clase de yoga")
    elif 19 < hora < 22:
        print("Hay body combat")
    else:
        print("No hay clase ahora mismo")
elif dia == "MARTES" or dia == "JUEVES":
    if 12 <= hora < 14:
        print("Hay clase de yoga")
    elif 16 <= hora < 20:
        print("Hay clase de spinning")
    elif 19 < hora < 22:
        print("Hay body combat")
    else:
        print("No hay clase ahora mismo")
elif dia == "SABADO" or dia == "DOMINGO":
    print("Está cerrado")   
else:
    print("Tienes que decirme un dia de la semana")
    