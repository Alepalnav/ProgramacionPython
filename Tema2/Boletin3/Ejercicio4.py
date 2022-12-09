
a = "Python900"
b = 900
def numberInString(a):
    contador = 0
    for i in a:
        for x in range(0,9+1):
            x = str(x)
            if i == x:
                contador += 1
    return contador

print(numberInString(a))

        





































