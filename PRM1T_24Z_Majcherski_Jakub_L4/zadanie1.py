import math 


def funkcja(n,x):
    suma=0
    for i in range(0,n):
        wyraz=((-1)**i)/(math.factorial(2*i))*(x**(2*i))
        suma=suma+wyraz
    return suma


for i in range(2,11):
    print(funkcja(i,math.pi/4))

