
menu = ''' a. Sumar dos fracciones.
b. Restar dos fracciones.
c. Multiplicar dos fracciones.
d. Dividir dos fracciones.
e. Salir.
'''

def sumar_fracciones(f1,f2):
    for i in range(len(f1)):
        if f1[i] == "/":
            n1 = int(f1[:i])
            d1 = int(f1[i+1:])
    for x in range(len(f2)):
        if f2[x] == "/":
            n2 = int(f2[:x])
            d2 = int(f2[x+1:])
    n = n1*d2+d1*n2
    d = d1*d2
    resultado = str(n)+"/"+str(d)
    return resultado

def restar_fracciones(f1,f2):
    for i in range(len(f1)):
        if f1[i] == "/":
            n1 = int(f1[:i])
            d1 = int(f1[i+1:])
    for x in range(len(f2)):
        if f2[x] == "/":
            n2 = int(f2[:x])
            d2 = int(f2[x+1:])
    n = n1*d2-d1*n2
    d = d1*d2
    resultado = str(n)+"/"+str(d)
    return resultado

opcion = input(menu)

while opcion != "e":
    if opcion == "a":
        f1 = input("Dime la primera fraccion")
        f2 = input("Dime la segunda fraccion")
        print(sumar_fracciones(f1, f2))
    if opcion == "b":
        f1 = input("Dime la primera fraccion")
        f2 = input("Dime la segunda fraccion")
        print(restar_fracciones(f1, f2))






























