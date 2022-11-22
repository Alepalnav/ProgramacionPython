lista = ["hola",2,3,4,5]

def reverse(lista):
    n = 0
    lista2 = []
    while n < len(lista):
        n += 1
        lista2.append(lista[(len(lista))-n])
    return lista2

print(reverse(lista))
