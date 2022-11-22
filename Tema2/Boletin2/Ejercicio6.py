num = -55
numeros = ["0","1","2", "3", "4","5","6","7","8","9"]
def getNumberOfDigits(num, numeros):
    num1 = str(num)
    digitos = 0
    for i in num1:
        if i in numeros :
            digitos += 1
        else:
            pass
    return digitos

print(getNumberOfDigits(num, numeros))
