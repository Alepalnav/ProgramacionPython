'''
Created on 31 oct. 2022

@author: Ale Palma
'''

tamagno = int(input("Dime el tamaño de la empresa: "))

contEdadpy = 0
contEdadja = 0
hombresPython = 0
mujeresPython = 0
hombresJava = 0
mujeresJava = 0
python = 0
java = 0
tamagnopy = 0
tamagnoja = 0

contador = 1

while contador <= tamagno:
    print("Nuevo empleado, introduzca sus datos: ")
    edad = int(input("Dime tu edad: "))
    while edad > 65 or edad < 18:
        edad = int(input("No válido, repite el dato: "))
    sexo = input("Dime tu sexo(H-M): ")
    while sexo != "H" and sexo != "M":
        sexo = input("No válido, repite el dato: ")
    leng = input("Dime tu lenguaje de programación habitual: ")
    while leng != "python" and leng != "java":
        leng = input("No válido, repite el dato: ")
    if sexo == "H" and leng == "python":
        hombresPython += 1
        python += 1
        contEdadpy += edad
        tamagnopy += 1
    elif sexo == "H" and leng == "java":
        hombresJava += 1
        java += 1
        contEdadja += edad
        tamagnoja += 1
    elif sexo == "M" and leng == "python":
        mujeresPython += 1
        python += 1
        contEdadpy += edad
        tamagnopy += 1
    elif sexo == "M" and leng == "java":
        mujeresJava += 1
        java += 1
        contEdadja += edad
        tamagnoja += 1
    contador += 1
    
mediaEdadpy = contEdadpy / tamagnopy 
mediaEdadja = contEdadja / tamagnoja
porPython = (python / tamagno) *100
porJava = (java / tamagno) * 100

print("El "+ str(porPython)+"% de empleados utiliza python, de los que "+ str(hombresPython)+ " son hombres y "+ str(mujeresPython)+ " mujeres y su edad media "+str(mediaEdadpy)+" años")
print("El "+ str(porJava)+"% de empleados utiliza java, de los que "+ str(hombresJava)+ " son hombres y "+ str(mujeresJava)+ " mujeres y su edad media "+str(mediaEdadja)+" años")