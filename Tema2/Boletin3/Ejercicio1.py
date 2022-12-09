
a = "programacion".upper()
n = input("Dime un caracter: ")


def charactersInString(a, n):
    contador = 0
    for i in a:
        if i == n:
            contador += 1
    return contador 
   
print(charactersInString(a, n))

   
   
   
   
   
   
   
   
   
    