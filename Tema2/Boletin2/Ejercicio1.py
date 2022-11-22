n = 5

def computeFactorial(n):
    if n > 0:
        suma = 1
        for i in range(1, n + 1):
            suma *= i
        return suma
    else:
        return None
    
print(computeFactorial(n))