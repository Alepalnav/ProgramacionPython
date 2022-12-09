nombre = "Enriqueta"
apellido1 = "Rodriguez"
apellido2 = "Montessori"
dni = "45676754L"

def generar_usuario(nombre, apellido1, apellido2, dni):
    resultado = ""
    resultado += nombre[:3].lower()
    resultado += apellido1[-3:].lower()
    resultado += apellido2[:3].lower()
    resultado += dni[-5:-1]
    return resultado

print(generar_usuario(nombre, apellido1, apellido2, dni))

n = int(input("Dime un numero 1-6: "))
lista = ["","","","",""]
contador = 1
numero = 5

while 1 <= n < 6:
    if n == 1:
        usuario = input("dime un usuario: ")
        lista[(contador%numero)-1] = usuario
        contador += 1
    elif n == 2:
        usuario = input("dime un usuario: ") 
        if usuario in lista:
            for i in range(len(lista)):
                if lista[i] == usuario:
                    lista[i] = ""
        else:
            print("este usuario no existe en la lista: ")
    elif n == 3:
        nombre = input("Nombre: ")
        apellido1 = input("Apellido 1: ")
        apellido2 = input("Apellido 2: ")
        dni = input("Dni: ")
        usuario = generar_usuario(nombre, apellido1, apellido2, dni)
        lista[(contador%numero)-1] = usuario
        contador += 1
    elif n == 4:
        print(lista)
    elif n == 5:
        lista = ["","","","",""]
    n = int(input("Dime un numero 1-6: "))










