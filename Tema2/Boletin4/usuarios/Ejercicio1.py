
mensaje = '''
1. Iniciar: 
2. Registrarse:
3. Mostrar usuarios:
4. Salir:  
'''
 
usuarios = ["ale","","","","","","","","",""]
contraseñas = ["hola","","","","","","","","",""]

def usuarios_contraseña(mensaje, usuarios, contraseñas):
    n = int(input(mensaje))
    while n != 4:
        if n == 1:
            contador_login = 0
            while contador_login < 3:
                user = input("Dime el usuario: ")
                for n in range(len(usuarios)):
                    if usuarios[n] == user:
                        contra = input("Dime la contraseña: ")
                        if contraseñas[n]== contra:
                            print("Inicio de sesión realizado")
                            contador_login += 1
                        else:
                            print("Contraseña incorrecta")
                    else:
                        print("No existe este usuario.")
        if n == 2:
            pass



print(usuarios_contraseña(mensaje, usuarios, contraseñas))
































