listaNombres = ["Alejandro", "Alvaro", "Paco"]
letra = "A"

def nombresLetra(listaNombres, letra):
    lista3 = []
    for i in listaNombres:
        if letra == i[0]:
            lista3.append(i)
    return lista3

print(nombresLetra(listaNombres, letra))
