lista = ["hola", "ordenador", "mundo","hxla", "ordenados"]

def compararLista(lista):
    elemento = lista[0]
    mayor = []
    for i in lista:
        if len(i) == len(elemento):
            palabra1 = []
            palabra2 = []
            cantidad1 = []
            cantidad2 = []
            for x in i:
                if x in palabra1:
                    cantidad1.append(x)
                palabra1.append(x)
            for y in elemento:
                if y in palabra2:
                    cantidad2.append(y)
                palabra2.append(y)
            if len(cantidad1) > len(cantidad2):
                mayor = [i] 
            elif len(cantidad2) > len(cantidad1):
                mayor = [elemento]                      
        if len(i) > len(elemento):
            elemento = i
            mayor = [i]
    return mayor

print(compararLista(lista))
