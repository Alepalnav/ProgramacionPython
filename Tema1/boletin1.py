
print("Ejercicio 1:")

print(7>=27 and not(7<=2))
print(24>5 and 10<=10 or 10==5)
print((10>=15 or 23==13) and not(8==8))
print(not(6/3>3) or 7>7)

print("-------")

print("Ejercicio 2:")

print(27 % 4 + 15/4)
print(37/ 4**2 -2)
print(9*2 /3*10*3)
print((7*3 - 4*4)**2/4*2)

print("-------")

print("Ejercicio 3:")

precio = 20
print(60 <= precio <= 420)

numero = 5
print(numero%2 == 1)

saldo = 20
dineroSacar = 30
print(saldo >=0 and saldo >= dineroSacar and dineroSacar > 0)

hora = 25
minutos = 23
print(0<=hora<24 and 0<=minutos<60)

estadoCivil = 'S'
print(not( estadoCivil == 'S' or estadoCivil == 'C' or estadoCivil == 'V' or estadoCivil == 'D'))

print("--------")

print("Ejercicio 4: ")

cantidad = 301
print(0 < cantidad < 300)

edad = 17
print(0 <= edad < 16 or 22 < edad)

respuesta = ("Si")
respuesta = ("No")
print(respuesta != ("Si") and respuesta != ("No"))

numero = 21
print(numero%7 != 0 or numero%3 != 0)

print("--------")

print("Ejercicio 5:")

print("Primera combinación:")
a = True 
b = True
print((a or b) and not(a))
print(not ( a or b)and b)
print(a or not b)
print(not ((a and b)and(b or a)))

print("Segunda:")
a = True
b = False

print((a or b) and not(a))
print(not ( a or b)and b)
print(a or not b)
print(not ((a and b)and(b or a)))

print("Tercera:")
a = False
b = True

print((a or b) and not(a))
print(not ( a or b)and b)
print(a or not b)
print(not ((a and b)and(b or a)))

print("Cuarta:")
a = False
b = False

print((a or b) and not(a))
print(not ( a or b)and b)
print(a or not b)
print(not ((a and b)and(b or a)))




