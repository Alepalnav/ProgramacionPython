'''
Función que dado un instante (horas, minutos y segundos) devuelva el número
de segundos transcurridos desde el inicio de un día hasta ese instante.
'''

instante = "21:22:12"

def segundos_transcurridos(instante):
    horas = int(instante[0:2])
    minutos = int(instante[3:5])
    segundos = int(instante[6:8])
    resultado = segundos + (minutos*60) + (horas*60*60)
    return str(resultado) + " segundos"

print(segundos_transcurridos(instante))




