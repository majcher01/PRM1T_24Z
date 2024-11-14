

def popraw(tekst):
    zdania=tekst.split(".")
    #petla usuwajaca puste elementy
    for i in range(0,len(zdania)):
        if(zdania[i]==""):
            zdania.pop(i)

    for i in range(0,len(zdania)):
        zdania[i]=zdania[i].strip()
        if(not zdania[i][0].isupper()):
            zdania[i]=zdania[i].replace(zdania[i][0],zdania[i][0].upper(),1)
        zdania[i]=zdania[i]+"."
    wynik=""
    for i in zdania:
        wynik=wynik+str(i)+" "
    wynik=wynik.strip()
    return wynik


def main():
    a="poszła Ola do przedszkola. zapomniała parasola . A parasol był popsuty, połamane wszystkie druty .w."
    print(popraw(a))

if __name__=="__main__":
    main()