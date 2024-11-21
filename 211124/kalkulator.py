import funkcje_kalkulatora as fk
import sys

if __name__=="__main__":
    if (len(sys.argv)>1):
        l1=int(sys.argv[1])
        operator=sys.argv[2]
        l2=int(sys.argv[3])
    else:
        l1=int(input("Podaj pierwsza liczbe "))
        operator=str(input("Podaj operator "))
        l2=int(input("Podaj druga liczbe "))

    operatory=["dodaj","odejmij","podziel","mnoz"]

    if operator not in operatory:
        exit("niepoprawny operator")
    
    match operator:
        case "dodaj":
            print("Wynik: "+str(l1)+" dodać "+str(l2)+" = "+str(fk.dodawanie(l1,l2)))
        case "odejmij":
            print("Wynik: "+str(l1)+" minus "+str(l2)+" = "+str(fk.odejmowanie(l1,l2)))
        case "podziel":
            print("Wynik: "+str(l1)+" podzielić na "+str(l2)+" = "+str(fk.dzielenie(l1,l2)))
        case "mnoz":
            print("Wynik: "+str(l1)+" razy "+str(l2)+" = "+str(fk.mnozenie(l1,l2)))