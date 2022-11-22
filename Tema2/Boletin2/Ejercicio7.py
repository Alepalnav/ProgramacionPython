num = 7

def isPrime(num):
    contador = 0
    if (type(num) == int) > 0:
        for i in range(1,num+1):
            if num%i == 0:
                contador += 1
        return contador == 2
    else:
        return None

print(isPrime(num))
