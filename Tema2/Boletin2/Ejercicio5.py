num1 = 2
num2 = 3

def powerIt(num1,num2):
    if type(num2) != int:
        return num1**0
    else:
        numero =  num1**num2
        return numero

print(powerIt(num1, num2))
