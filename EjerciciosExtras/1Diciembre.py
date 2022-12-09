

dni = "11111111H" 
letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z", "S", "Q", "V","H","L","C","K","E"]
numeros = [1,2,3,4,5,6,7,8,9]
def comprobarDni(dni, letras):
    validacion = True
    for i in range(len(dni)-1):
        if int(dni[i]) not in numeros:
            return False
    numero = dni[0:-1]
    letra = dni[-1:]
    n = int(numero)%23
    if (len(dni) != 9 and len(dni) != 8) and (letras[n] != letra):
        validacion = False
    return validacion

print(comprobarDni(dni, letras))





























