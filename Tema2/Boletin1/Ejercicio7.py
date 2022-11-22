ficha1 = [3,4]
ficha2 = [2,4]

def encajan(ficha1, ficha2):
    mensaje = "No es correcto"
    if (ficha2[0] == ficha1[0] or ficha2[1] == ficha1[0]) or (ficha2[0] == ficha1[1] or ficha2[1] == ficha1[1]):
            mensaje = "Es correcto"
    return mensaje 
        
print(encajan(ficha1, ficha2))
