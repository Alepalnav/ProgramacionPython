lista = [1,2,5,6]

a_escribir = lista[0]
a_guardar = 0

for i in range(len(lista)):
    a_guardar = lista[(i+1)%len(lista)] 
    lista[i+1] = a_escribir
    a_escribir = a_guardar
print(lista)
