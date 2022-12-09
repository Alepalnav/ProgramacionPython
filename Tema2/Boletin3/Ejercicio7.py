'''
Created on 28 nov. 2022

@author: Ale Palma
'''

frase = "Hacer siguiente boletin"
palabra_buscar = "siguiente"
palabra_sustituta = "anterior"


def sustituir(frase,palabra_buscar,palabra_sustituta):
    ind_pal_buscar = 0
    resultado, tmp = "", ""
    
    for i in range(len(frase)):
        if frase[i] == palabra_buscar[ind_pal_buscar]:
            if ind_pal_buscar == len(palabra_buscar)-1:
                tmp = ""
                resultado += palabra_sustituta
                ind_pal_buscar = 0
            else:
                tmp += frase[i]
                ind_pal_buscar += 1
        else:
            resultado += tmp+frase[i]
            ind_pal_buscar = 0
            tmp = ""
    return resultado
               
print (sustituir(frase,palabra_buscar,palabra_sustituta))


