listanum = []

for i in range(100):
    numero = randint(0,1000)
    listanum.append(numero)
    
def mayor(listanum):
    maxi = listanum[0]
    for x in listanum:
        if x > maxi:
            maxi = x 
    return maxi   

print(mayor(listanum))
    
def menor(listanum):
    men = listanum[0]
    for x in listanum:
        if x < men:
            men = x 
    return men

print(menor(listanum))

def suma(listanum):
    sumar = 0
    for x in listanum:
        sumar += x
    return sumar

print(suma(listanum))

def media(listanum):
    sumar = 0
    for x in listanum:
        sumar += x 
    return sumar//len(listanum)

print(media(listanum))

def cambiar(listanum):
    n = int(input("dime un numero para cambiar: "))
    numero = randint(1,100)
    listanum[numero] = n
    return listanum

print(cambiar(listanum))
       
print(listanum)