numbers = int(input("How many numbers do you want input?"))
contador = 0

while numbers <= 0:
    numbers = int(input("How many numbers do you want input"))
    
for n in range(numbers):
    number = int(input("Enter one number greater than 0:"))
    while number <= 0:
        number = int(input("The number is not valid, it should be greater than 0"))
        contador += number
    else:
        contador += number
media = float(contador / numbers)
print("The medium is "+ str(media))
    
