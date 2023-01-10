
nombre = "Enriqueta"
apellido1 = "Rodriguez"
apellido2 = "Montessori"
dni = "45676754L"

def generar_usuario(nombre,apellido1, apellido2, dni):
    resultado = ""
    resultado += nombre[:3]
    resultado += apellido1[-3:]
    resultado += apellido2[:3]
    resultado += dni[-5:-1]
    return resultado.lower()

assert(generar_usuario(nombre, apellido1, apellido2, dni)=="enruezmon6754")

lista = ["","","","",""]

menu = '''
1. Añadir usuario: 
2. Eliminar usuario:
3. Crear usuario: 
4. Consultar usuarios: 
5. Borrar usuarios:
6. Salir:
'''

n = int(input(menu))
contador = 0

while n != 6:
    if n == 1:
        usuario = input("Dime un usuario a añadir: ")
        lista[contador%5]=usuario
        contador += 1
    elif n == 2:
        usuario = input("Dime un usuario a eliminar: ")
        if usuario in lista:
            for i in range(len(lista)):
                if lista[i] == usuario:
                    lista[i]=""
        else:
            print("Este usuario no existe.")
    elif n == 3:
        nombre = input("Dime un nombre: ")
        apellido1 = input("Dime un apellido: ")
        apellido2 = input("Dime otro apellido: ")
        dni = input("Dime un dni: ")
        lista[contador%5]=generar_usuario(nombre, apellido1, apellido2, dni)
        contador += 1
    elif n == 4:
        print(lista)
    elif n == 5:
        lista = ["","","","",""]
    n = int(input(menu))
























