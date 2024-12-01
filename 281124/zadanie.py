#zrobione nie w terminie

import os

wybor=0

def wczytajplik(nazwa):
    global plikname
    plikname=nazwa
    global plik
    if(not os.path.isfile(nazwa)):
        exit(print("niemapliku"))
    plik=open(nazwa, "r+")

def wyswietllinie(n):
    l=plik.readlines()
    print(l[n-1])

def wyswietlcalosc():
    print(plik.read())

def zamienlinie(n,tresc):
    global l
    l=plik.readlines()
    for i in range(len(l)):
        l[i]=l[i].strip()
    l[n-1]=tresc
    print(l)

def zapisz():
    plik=open(plikname,"w")
    for i in l:
        plik.write(i+"\n")
    plik.close()

def nowy(nazwa):
    open(nazwa,"a+").close()

while True:
    print("""
    [1] - Wczytaj plik
    [2] - Wyswietl linijke
    [3] - Wyswietl calosc
    [4] - Zamien linijke
    [5] - Zapisz plik
    [6] - utworz nowy plik
    [7] - Zakoncz
    """
    )
    wybor=int(input("Wybierz operacje: "))

    match wybor:
        case 1:
            nazwapliku=str(input("Podaj nazwe pliku: "))
            wczytajplik(nazwapliku)
        case 2:
            linia=int(input("Podaj linie: "))
            wyswietllinie(linia)
        case 3:
            wyswietlcalosc()
        case 4:
            linia=int(input("Podaj linie: "))
            tresc=str(input("Podaj nowa tresc: "))
            zamienlinie(linia,tresc)
        case 5:
            zapisz()
        case 6:
            n=str(input("Podaj nazwe: "))
            nowy(n)
        case 7:
            break


