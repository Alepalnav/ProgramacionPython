print("Ejercicio 9: ")

lista = [1,4,2,6,8,10]
k = 5

def menor(lista, k):
    lista2 = []
    for i in lista:
        if i < k:
            lista2.append(i)
    return lista2


def mayor(lista, k):
    lista3 = []
    for x in lista:
        if x > k:
            lista3.append(x)
    return lista3

def multiplos(lista, k):
    lista4 = []
    for n in lista:
        if n%k == 0:
            lista4.append(n)
    return lista4 

print(menor(lista, k))
print(mayor(lista, k))
print(multiplos(lista, k))




























