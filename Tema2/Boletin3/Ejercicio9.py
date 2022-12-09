'''
Created on 28 nov. 2022

@author: Ale Palma
'''
a = "curso de programacion"
vocales = "aeiou"
blanco = " "

def construirCadena(a,vocales,blanco):
    vocal = ""
    cadena = ""
    for i in a:
        if i not in vocales and i not in blanco:
            cadena += i
        if i in vocales:
            vocal += i
    cadena += vocal
    return cadena

assert(construirCadena(a, vocales, blanco) == "crsdprgrmcnuoeoaaio")
print(construirCadena(a, vocales, blanco))
