str1="""
Wybierz tryb:\n
Dodaj pracownika [1]
Usun pracownika [2]
Wyswietl liczbe pracownikow [3]
\n
Wyjscie [4]
"""

pracownicy=[]


while True:
    tryb=int(input(str1))


    if(tryb==1):
        dane=str(input("Wpisz dane oddzielone spacja:\n"))
        temp = dane.split(" ")
        slownik=dict()
        for i in range(0,(len(temp))):
            slownik[i]=temp[i]
        pracownicy.append(slownik)
    elif(tryb==2):
        nazwisko=str(input("Podaj nazwisko: "))
        for i in range(0,len(pracownicy)):
            if(pracownicy[i][1]==nazwisko):
                pracownicy.pop(i)
    elif(tryb==3):
        for i in pracownicy:
            print(i[0]+" "+i[1]+"\n\tZatrudniony jako: "+i[2]+"\n\tStaz pracy: "+str(2024-int(i[3])))

    elif(tryb==4):
        break;
    else:
        print("nieznany tryb")