'''
Crea una función que devuelva la diferencia en segundos entre dos instantes de
tiempo del mismo día. Recibirá como parámetros seis valores, hora, minuto y
segundo de cada uno de los instantes.

'''

instante1 = "22:10:23"
instante2 = "16:20:12"

def diferencia_segundos(instante1,instante2):
    horas1 = int(instante1[0:2])
    minutos1 = int(instante1[3:5])
    segundos1 = int(instante1[6:8])
    horas2 = int(instante2[0:2])
    minutos2 = int(instante2[3:5])
    segundos2 = int(instante2[6:8])
    total1 = segundos1 + (minutos1*60) + (horas1*60*60)
    total2 = segundos2 + (minutos2*60) + (horas2*60*60)
    if total1 > total2:
        resultado = total1 - total2
    else:
        resultado = total2 - total1
    return resultado

print(diferencia_segundos(instante1, instante2))