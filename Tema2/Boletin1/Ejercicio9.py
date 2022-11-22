lista = [1,4,2,5,6]
k = 5

def menores(lista,k):
    menor = []
    for i in lista:
        if i < k:
            menor.append(i)
    return menor

print(menores(lista, k))
            
def mayores(lista,k):
    mayor = []
    for i in lista:
        if i > k:
            mayor.append(i)
    return mayor

print(mayores(lista, k))

def multiplos(lista,k):
    multiplo = []
    for i in lista:
        if i%k == 0:
            multiplo.append(i)
    return multiplo

print(multiplos(lista, k))
