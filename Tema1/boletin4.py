
print("Ejercicio 1: ")

cateto1 = int(input("Dime el cateto 1:"))
cateto2 = int(input("Dime el cateto 2:"))

hipotenusa = ((cateto1**2)+(cateto2**2))**(1/2)

print(hipotenusa)

print("--------")

print("Ejercicio 2: ")

fahr = int(input("Dime los grados Fahrenheit: "))

celsius = (fahr - 32) * (5/9)

print("Son " + str(celsius)+ " grados")

print("--------")

print("Ejercicio 3: ")

num1 = int(input("Dime un numero: "))
num2 = int(input("Dime otro: "))
num3 = int(input("Dime otro: "))

media = (num1 + num2 + num3)/3

print("La media es " + str(media))

print("-------")

print("Ejercicio 4: ")

precio = int(input("Dime el precio inicial: "))

preciofinal = precio - (precio * (15/100))

print("El precio final es "+ str(preciofinal))

print("-------")

print("Ejercicio 5: ")

num1 = int(input("Dime un numero: "))
num2 = int(input("Dime otro numero: "))
distancia = (abs(num1 - num2))
print("La distancia es: " + str(distancia))

print("-------")

print("Ejercicio 6: ")

x1 = int(input("Dime un punto x: "))
y1 = int(input("Dime su punto y: "))
x2 = int(input("Dime otro punto x: "))
y2 = int(input("Dime su punto y: "))

distancia = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print(distancia)

print("-------")

print("Ejercicio 7: ")

numero = int(input("Dime un numero: "))

cuadrado = numero**(1/2) 
cubica = numero**(1/3)

print("La raiz cuadrada de " + str(numero) + " es " + str(cuadrado)+ " y la cubica es " + str(cubica))

print("-------")

print("Ejercicio 8: ")

doseuros = int(input("cuantas monedas de dos euros:")) *2
euro = int(input("cuantas monedas de euro:"))
cincocent = int(input("cuantas monedas de cincuenta cent:")) *(1/2)
veintecent = int(input("cuantas monedas de veinte cent:")) *(1/5)
diezcent = int(input("cuantas monedas de diez cent:")) * (1/10)

total = doseuros + euro + cincocent + veintecent + diezcent
euros = int(total)
cent = (total - euros)*100
print("Tenemos " + str(euros)+ " euros y "+ str(int(cent))+ " centimos") 

print("--------")

print("Ejercicio 9: ")

base = int(input("Dime la base: "))
exponente = int(input("Dime el exponente: "))
potencia = base ** abs(exponente) 

if exponente > 0: 
    print(potencia)
elif exponente == 0:
    potencia == 1
    print(potencia)
else: 
    potencia = 1/potencia 
    print(potencia)

print("--------")


print("Ejercicio 10: ")

a = int(input("Dime la dimensi??n de un lado: "))
b = int(input("Dime otro: "))
c = int(input("Dime otro: "))

if a**2 + b**2 == c**2:
    print("triangulo rectangulo")
elif a == b == c:
    print("triangulo equil??tero")
elif a == b or a == c or b == c:
    print("Triangulo is??sceles")
else:
    print("Triangulo escaleno")    

print("-------")

print("Ejercicio 11:")

a??o = int(input("Dime un a??o: "))

if a??o%4 == 0:
    if a??o%400 == 0:
        print("Es un a??o bisiesto")
    elif a??o%100 == 0:
        print("No es a??o bisiesto")
    else:
        print("Es un a??o bisiesto")
else:
    print("No es a??o bisiesto")

print("-------")

print("Ejercicio 12: ")

tipo = input("Dime el tipo de uva: ")
tipo1 = tipo.upper()
tama??o = int(input("Dime el tama??o: "))

if tipo1 == "A":
    if tama??o == 1:
        print("Se le cargan 20 cents al precio inicial")
    elif tama??o == 2:
        print("Se le cargan 30 cents al precio inicial")
    else: 
        print("No existe ese tama??o")
elif tipo1 == "B":
    if tama??o == 1:
        print("Se le rebajan 30 cents al precio inicial")
    elif tama??o == 2:
        print("Se le rebajan 50 cents al precio inicial")
    else: 
        print("No existe ese tama??o")
else:
    print("No existe ese tipo")
 



print("-------")


print("Ejercicio 13: ")

alumnos = int(input("??Cu??ntos alumnos viajan?: "))

if alumnos >= 100:
    print("Los alumnos deben pagar 65 euros cada uno")
    print(("el director pagar??: ")+str(alumnos*65))
elif 49 < alumnos < 100:
    print("Los alumnos deben pagar 70 euros cada uno") 
    print(("el director pagar??: ")+str(alumnos*70))
elif 29 < alumnos < 50:
    print("Los alumnos deben pagar 95 euros cada uno")
    print(("el director pagar??: ")+str(alumnos*95))
elif 0 < alumnos < 30:
    print("Los alumnos deben pagar "+ str(4000/alumnos)+ "euros cada uno")
    print("el director pagar??: 4000")
else: 
    print("el numero de alumnos debe ser positivo")

print("---------")

print("Ejercicio 14:")

minuto = int(input("??Cu??nto ha durado la llamada?: "))
dia1 = input("??Que dia es?")
dia = dia1.upper()
#turno = input("??Es por la ma??ana o por la tarde?")
restante = minuto - 5
restante1 = restante - 3 
restante2 = restante1 - 2

if minuto < 5:
    print(minuto*1)
elif 5 < minuto < 9:
    print((5 * 1)+ (restante * 0.80))
elif 8 < minuto < 11:
    print((5*1)+ (3 * 0.80) + (restante1 * 0.70))
elif 10 < minuto:
    print((5*1)+ (3 * 0.80) + (2 * 0.70)+(restante2*0.50))
    




print("Ejercicio 15:")

dia = int(input("Dime un numero del 1 al 7: "))
if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
    print("Es sabado")
elif dia == 7:
    print("Es domingo")
else:
    print("error")



print("Ejercicio 16:")

mes = int(input("Dime el numero del mes: "))

if 0 < mes < 8:
    if mes == 2:
        print("Tiene 28 dias")
    elif mes%2== 0:
        print("Tiene 30 dias")
    elif mes%2 != 0:
        print("Tiene 31 dias")
elif 7 < mes < 12:
    if mes%2== 0:
        print("Tiene 31 dias")
    elif mes%2 != 0:
        print("Tiene 30 dias")
else:
    print("Tiene que ser entre 1 y 12")
    








