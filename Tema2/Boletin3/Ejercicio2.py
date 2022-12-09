

a = "Boletin"

def lowCaseInString(a):
    contador = 0
    for i in a:
        if str.islower(i):
            contador += 1
    return contador

print(lowCaseInString(a))




















