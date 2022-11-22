lista1 = [1,3,4,6]
lista2 = [1,2,4,7]

def unionLista(lista1,lista2):
    lista3 = []
    for i in lista2:
        lista3.append(i)
    for i in lista1:
        if i not in lista2:
            lista3.append(i)
    lista3.sort()
    return lista3

print(unionLista(lista1, lista2))
