'''
print("Ejercicio 1:")
num=int(input("Dime un número: "))
if num%2 == 0:
    print("Es par")
else: 
    print("Es impar")
    
print("--------")

print("Ejercicio 2:")

num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número"))

if num1 == num2:
    print("Son iguales")
elif num1 > num2:
    print("El primer número es mayor")
else:
    print("El segundo número es mayor")
    
print("---------")
'''
print("Ejercicio 3:")

numero = int(input("Dime un número: "))

if numero%2 == 0:
    print("El número "+ str(numero) + " es múltiplo de 2")
if numero%3 == 0:
    print("El número "+ str(numero)+ " es múltiplo de 3")
'''
print("--------")

print("Ejercicio 4:")

edad = int(input("Dime tu edad: "))

if edad < 100:
    if edad <= 12 and edad > 0:
        print("Eres un niño")
    elif edad >= 13 and edad <= 17:
        print("Eres adolescente")
    elif edad >= 18 and edad <= 29:
        print("Eres joven")
    else:
        print("Eres adulto")

print("-------")

print("Ejercicio 5:")

numero1 = int(input("Dime un número: "))
numero2 = int(input("Dime un número: "))
numero3 = int(input("Dime un número: "))
numero4 = int(input("Dime un número: "))

media = (numero1 + numero2+ numero3+ numero4)/4
print(media)

if numero1 > media:
    print("El número %s es superior a la media" % (numero1))
if numero2 > media:
    print("El número "+ str(numero2)+ " es superior a la media")
if numero3 > media:
    print("El número "+ str(numero3)+ " es superior a la media")
if numero4 > media:
    print("El número "+ str(numero4)+ " es superior a la media")
    
print("--------")

print("Ejercicio 6:")

letra = input("Dime una letra")
letras = letra.upper()

vocal1 = "A"
vocal2 = "E"
vocal3 = "I"
vocal4 = "O"
vocal5 = "U"
if letras == vocal1:
    print("Es la primera vocal(A)")
elif letras == vocal2:
    print("Es la segunda vocal(E)")
elif letras == vocal3:
    print("Es la tercera vocal(I)")
elif letras == vocal4:
    print("Es la cuarta vocal(O)")
elif letras == vocal5:
    print("Es la quinta vocal(U)")
else: 
    print("No es vocal")

print("--------")

print("Ejercicio 7:")

estado = input("Dime tu estado civil: ")
estadoCivil = estado.upper()
edad = 29

if edad > 50:
    print("8.5%")
elif estadoCivil == 'S' or estadoCivil == 'D' and edad < 35:
    print("12%")
elif estadoCivil == 'V' or estadoCivil == 'C' and edad < 35:
    print("11.3%")
else:
    print("10.5%")

print("-------")
'''

print("Ejercicio 8: ")

hora1 = int(input("hora1: "))
minuto1 = int(input("minuto1: "))
segundo1 = int(input("segundo1: "))
hora2 = int(input("hora2: "))
minuto2 = int(input("minuto2: "))
segundo2 = int(input("segundo2: "))

if 0 < hora1 < 24 and 0 < hora2 < 24:
    if hora1 > hora2:
        print("Hora 1 es mayor")
    elif hora2 > hora1:
        print("Hora 2 es mayor")
    elif 0 < minuto1 < 60 and 0 < minuto2 < 60:
        if minuto1 > minuto2:
            print("Hora 1 es mayor")
        elif minuto2 > minuto1:
            print("Hora 2 es mayor")
        elif 0 < segundo1 < 60 and 0 < segundo2 < 60:   
                if segundo1 > segundo2:
                    print("Hora 1 es mayor")
                elif segundo2 > segundo1: 
                    print("Hora 2 es mayor")
                else: 
                    print("Son iguales")
        
     

print("---------") 
'''
print("Ejercicio 9: ")

tipo = input("Dime el tipo de producto: ")
tipos = tipo.upper()
precio = int(input("Dime su precio original: "))
tipo1 = "A"
tipo2 = "B"
tipo3 = "C"
descuento1 = precio*(7/100)
descuento2 = precio*(12/100)
descuento3 = precio*(9/100)

if tipos == tipo1:
    print(precio-descuento1)
elif tipos == tipo2 or precio<500:
    print(precio-descuento2)
else:
    print(precio-descuento3)

print("-------")


print("Ejercicio 10:")

numero1 = int(input("Dime un número: "))
numero2 = int(input("Dime otro número: "))
operador = input("Dime un operador: ")

if operador == "+":
    print(numero1 + numero2)
elif operador == "*":
    print(numero1 * numero2)
elif operador == "-":
    print(numero1 - numero2)
elif operador == "/":
    print(numero1 / numero2)
else:
    print("Error")

'''  



