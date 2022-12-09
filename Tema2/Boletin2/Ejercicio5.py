num1 = 2
num2 = 5

def powerIt(num1,num2):
    contador = 0
    numero = 1
    if type(num2) != int:
        return num1**0
    else:
        while contador < num2:
            numero *= num1
            contador += 1
        return numero

print(powerIt(num1, num2))
