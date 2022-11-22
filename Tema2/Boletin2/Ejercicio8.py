from math import sqrt

a = 1
b = 4
c = 3

def solveSecondOrderEquation(a,b,c):
    if not(((b**2)-4*a*c) > 0):
        return None
    else:
        x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)  
        x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)  
        print("Las soluciones de la ecuación son:")
    return x1,x2

print(solveSecondOrderEquation(a, b, c))