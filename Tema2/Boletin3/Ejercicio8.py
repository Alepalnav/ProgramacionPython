'''
Created on 28 nov. 2022

@author: Ale Palma
'''

a = "Ejercicio 8 del boletin 3"
vocales = ["a","e","i","o","u"]

def buscarVocal(a,vocales):
    contador = []
    for i in a:
        i = i.lower()
        if i in vocales:
            if i not in contador:
                contador.append(i)
    return len(contador)
    

print(buscarVocal(a,vocales))