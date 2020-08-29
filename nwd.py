import math
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    else:
        return a
    
a = int(input("a: "))
b = int(input("b: "))

print("nwd liczb: "+str(a)+" i "+str(b)+" to: "+str(nwd(a,b)))
