lista1 = [1,4,5,6]
lista2 = [4,5,7,1,1]

def intersect(lista1,lista2):
    lista3 = []
    for i in lista1:
        if i in lista2:
            lista3.append(i) 
    return lista3

print(intersect(lista1, lista2))
