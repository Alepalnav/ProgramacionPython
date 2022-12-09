
def sum_digits(n):
    resultado = 0
    for i in str(n):
        resultado += int(i)
    return resultado    


assert(sum_digits(73) == 10)
assert(sum_digits(293883) == 33) 
assert(sum_digits(102) == 3)
print(sum_digits(23))















