a1 = int(input("Podaj a1: "))
r = int(input("Podaj r: "))
n = int(input("Podaj liczbe wyrazow: "))

suma=0
for i in range(0, n):
    wyraz = a1 + i * r
    suma=suma+wyraz
    print("Wartosc wyrazu: ", wyraz, " Suma: ", suma)
