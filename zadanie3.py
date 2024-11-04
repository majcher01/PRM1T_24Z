n = int(input("Podaj n: "))

for i in range(2, int(n / 2)+1):
    if (n % i) == 0:
        print("N nie jest liczba pierwsza")
        break
else:
    print("N jest liczba pierwsza")
