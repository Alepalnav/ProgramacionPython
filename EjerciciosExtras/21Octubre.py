
peso = float(input("¿Peso?: "))

while 0 < peso < 500:  
    edad = int(input("¿Edad?: "))
    while edad<0 or edad>110:
        edad = int(input("¿Edad?: "))
    tipo = input("¿Tipo de vida? (Sedentaria/Activa/Muy activa): ")
    tipo = tipo.upper()
    while not(tipo=="SEDENTARIA" or tipo=="ACTIVA" or tipo=="MUY ACTIVA"):
        tipo = input("¿Tipo de vida? (Sedentaria/Activa/Muy activa): ")
        tipo = tipo.upper()
    if (0<edad<110) and (tipo=="SEDENTARIA" or tipo=="ACTIVA" or tipo=="MUY ACTIVA"):
        if edad > 70 and tipo == "SEDENTARIA":
            print("Debe ir al médico")
        elif peso > 100:
            print("Debe ir al médico")
        elif peso > 74.4 and edad > 50:
            print("Debe ir al médico")
        else:
            print("No es urgente que acuda al médico si no tiene problemas de salud")
    peso = float(input("¿Peso?: "))
    
        
        
        