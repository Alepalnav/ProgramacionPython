lista = [2,3,7,9,15]

def estaOrdenada(lista):
    n = 1
    prueba = 0
    while n < len(lista):
        if lista[n] > lista[n-1]: 
            prueba += 1   
        n += 1
    return prueba == 4

print(estaOrdenada(lista))
