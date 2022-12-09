
def mcd(n,i):
    div_n = []
    div_i = []
    div_com = []
    for x in range(1,n+1):
        if n%x == 0:
            div_n.append(x)
    for y in range(1,i+1):
        if i%y == 0:
            div_i.append(y)
    for z in div_n:
        if z in div_i:
            div_com.append(z)
    return div_com[-1]

print(mcd(1024,248))            




























