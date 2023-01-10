'''
Función tal que dadas las coordenadas de dos puntos en el plano devuelve su
distancia euclídea. Un punto en el plano tiene dos coordenadas (abscisa y
ordenada), por lo tanto, la entrada a esta función son cuatro valores reales.

'''
from math import sqrt

x1 = 2
y1 = 4
x2 = 8
y2 = 10

def distancia_euclidea(x1,y1,x2,y2):
    formula = sqrt(((x2-x1)**2)+((y2-y1)**2))
    return formula

print(distancia_euclidea(x1, y1, x2, y2))



































