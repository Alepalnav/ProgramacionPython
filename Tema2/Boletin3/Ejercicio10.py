'''
Created on 28 nov. 2022

@author: Ale Palma
'''
a = "He estudiado mucho "

def numPalabras(a):
    contador = 1
    for i in range(len(a)):
        if a[i] == " " and a[i-1] != " ":
            contador += 1
    if a[-1] == " " :
        contador -= 1
    return contador
            
        
print(numPalabras(a))







