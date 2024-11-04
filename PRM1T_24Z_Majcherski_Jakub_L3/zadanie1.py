import math

n = int(input("Podaj N: "))

for i in range(n, 0, -1):
    print("Wartosc: ", i, " Kwadrat: ", i**2, " Pierwiastek: ", math.sqrt(i))
