import os

if(not os.path.exists("./liczby")):
    os.mkdir("./liczby")

if(not os.path.exists("./liczby/even.txt")):
    open("./liczby/even.txt","w").close

if(not os.path.exists("./liczby/odd.txt")):
    open("./liczby/odd.txt","w").close

liczba=1
even=open("./liczby/even.txt","a")
odd=open("./liczby/odd.txt","a")


while liczba!=0:
    liczba=int(input("Podaj liczbe: "))
    if(liczba==0):
        continue
    elif(liczba%2==0):
        even.write(str(liczba)+" ")
    else:
        odd.write(str(liczba)+" ")
even.close()
odd.close()