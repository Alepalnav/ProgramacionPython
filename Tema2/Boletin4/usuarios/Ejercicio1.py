
menu = '''
1. Crear cuenta: 
2. Iniciar sesion: 
3. Mostrar usuarios: 
4. Salir:
'''

usuarios = []
contraseñas = []

opcion = int(input(menu))

while opcion != 4:
    if opcion == 1:
        if len(usuarios) < 10:
            usuario = input("Escribe un usuario:")
            if usuario not in usuarios:
                contraseña1 = input("Escribe una contraseña: ")
                contraseña2 = input("Vuelve a escribir la contraseña: ")
                while contraseña1 != contraseña2:
                    contraseña2 = input("Vuelve a escribir la contraseña: ")
                usuarios.append(usuario)
                contraseñas.append(contraseña1)
            elif usuario in usuarios:
                print("Este usuario ya existe.")
    elif opcion == 2:
        usuario = input("Escribe un usuario:")
        contador = 0
        while contador < 3:
            if usuario in usuarios:
                contraseña = input("Escribe la contraseña: ")
                if contraseña in contraseñas:
                    print("Has iniciado sesion correctamente.")
                    contador += 3
                else:
                    contraseña = input("Escribe correctamente la contraseña: ")
                    contador += 1
            else:
                usuario = input("Vuelva a introducir correctamente el usuario: ")
                contador += 1
    elif opcion == 3:
        print(usuarios)
    
    opcion = int(input(menu))

print("Ha salido con éxito")























