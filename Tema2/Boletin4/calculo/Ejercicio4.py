
def calculo(n,i):
    resultado = 0
    for i in range(1,i+1):
        res = str(n)*i
        resultado += int(res)
    return resultado


print(calculo(1, 5))


























