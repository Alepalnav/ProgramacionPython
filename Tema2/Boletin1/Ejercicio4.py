def leerNumerosPar():
    lista = []
    n = int(input("Dime un numero: "))
    while n > 0:
        if n%2 == 0:
            lista.append(n)
        n = int(input("Dime un numero: "))
    mayor = lista[0]
    for i in lista:
        if i > lista[0]:
            mayor = i
    return lista, mayor

print(leerNumerosPar())
