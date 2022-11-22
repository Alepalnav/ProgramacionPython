numero = "101101B"

def conversor(numero):
    lista2 = []
    if numero[-1] == "B":
        numero = numero[0:len(numero)-1]
        for i in numero:
            if int(i) > 1:
                assert Exception("Los numeros binarios no son mayores que 1")
        n = 0
        for n in numero:
            lista2.append(n)
        x = 0
        y = len(lista2)-1
        producto = 0
        while x < len(lista2):
            producto += int(lista2[x]) * (2 ** y)
            x += 1
            y -= 1
        return producto
    if numero[-1] == "D":
        numero = numero[0:len(numero)-1]
        for i in numero:
            if not (0<=int(i)<9):
                assert Exception("La base decimal debe ser entre 0 y 9")
        numero = int(numero)
        binario = 0
        multiplicador = 1
        while numero != 0:
            binario += numero % 2 * multiplicador
            numero //= 2
            multiplicador *= 10
        return binario
print(conversor(numero))