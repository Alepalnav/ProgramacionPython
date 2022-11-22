dia = int(input("Introduce el dia de la fecha: "))
mes = int(input("Introduce el mes de la fecha: "))
anio = int(input("Introduce el año de la fecha: "))
listames = ["enero", "febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
diames = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]

def mes_letra(mes,listames):
    for i in listames:
        mes1 = listames[mes+1]
    return mes1
    
def frase(mes_letra,dia,anio):
    mensaje = ""
    while dia>0:
        mensaje = "La fecha en formato largo es "+str(dia)+" de "+str(mes_letra)+ " de "+str(anio)
    return mensaje

print(frase(mes_letra, dia, anio))
