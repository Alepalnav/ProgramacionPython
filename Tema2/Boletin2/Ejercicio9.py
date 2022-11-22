number = 50

def getPrimeDivisors(number):
    if type(number) != int:
        return None
    else:
        numeros = []
        for i in range(1,number+1):
            contador = 0
            for x in range(1,i+1):
                if i%x == 0:
                    contador += 1
            if contador == 2:
                numeros.append(i)
    return numeros

print(getPrimeDivisors(number))