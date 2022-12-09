

a = "ajboasbfhsolnsamna"
b = "hola"

def buscar(a,b):
    palabrab = ""
    for i in b:
        for x in a:
            if x == i:
                if x not in palabrab:
                    palabrab += x
    return palabrab == b
        
print(buscar(a, b))
'''
def buscar_palabra(palabra_buscar, lista):
    encontrada=False
    palabra=[]
    c=0
    c2=0
    while c<(len(lista)):
        if c2<(len(palabra)) and palabra_buscar[c2]==lista[c]:
            palabra.append(lista[c])
            c2+=1
        c+=1
    if c2==len(palabra_buscar):
        encontrada=True    
    return encontrada

print(buscar_palabra("hola", "shybaoxlna "))
print(buscar_palabra("zhola", "shybaoxlna"))
'''
















