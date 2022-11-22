num1 = 220
num2 = 284

def isFriendNumber(num1,num2):
    suma1 = 0
    suma2 = 0
    for i in range(1,num1+1):
        if num1%i == 0:
            suma1 += i
    for x in range(1,num2+1):
        if num2%x == 0:
            suma2 += x
    return suma1 == suma2

print(isFriendNumber(num1,num2))