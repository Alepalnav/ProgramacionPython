
def mcm(n1,n2):
    mul_n1 = []
    mul_n2 = []
    mul_com = []
    for n in range(1,n2+1):
        mul_n1.append(n1*n)
    for i in range(1,n1+1):
        mul_n2.append(n2*i)
    for m in mul_n1:
        if m in mul_n2:
            mul_com.append(m)
    return mul_com[0]


print(mcm(180,324))
























