a = "anilina"

def palindrome(a):
    a_reversed = ""
    for i in a:
        a_reversed = i + a_reversed
    if a_reversed == a:
        return True 
    else:
        return False

print(palindrome(a))



































