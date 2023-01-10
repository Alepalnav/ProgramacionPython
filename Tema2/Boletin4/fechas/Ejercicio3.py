'''
Write a Python program to convert seconds to day, hour, minutes and seconds.
'''

segundos = 75388

def convertir_segundos(segundos):
    minutos = 0
    horas = 0
    while segundos >= 60:
        minutos = segundos//60
        segundos = segundos%60
    while minutos >= 60:
        horas = minutos//60
        minutos = minutos%60
    resultado = str(horas)+":"+str(minutos)+":"+str(segundos)
    return resultado

print(convertir_segundos(segundos))











