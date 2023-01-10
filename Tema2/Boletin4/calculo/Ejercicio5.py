
n1 = 16
n2 = 6

def leer_fraccion(n1,n2):
    for i in range(1,n1):
        if (n1%i == 0) and (n2%i == 0):
            n1= n1//i
            n2= n2//i 
    resultado = n1,n2
    return resultado

print(leer_fraccion(n1, n2))

def escribir_fraccion(leer_fraccion):
    if n2 == 1:
        return n1
    else:
        return str(n1)+"/"+str(n2)

print(escribir_fraccion(leer_fraccion(n1,n2)))

def calcular_mcd(n1,n2):
    mcd1 = []
    mcd2 = []
    mcd = []
    for i in range(1,n1+1):
        if n1%i == 0:
            mcd1.append(i)
    for x in range(1,n2+1):
        if n2%x == 0:
            mcd2.append(x)
    for z in mcd2:
        if z in mcd1:
            mcd.append(z)
    return mcd[-1]

print(calcular_mcd(n1, n2))

n = 16/6

def simplificar_fraccion(n):
    













