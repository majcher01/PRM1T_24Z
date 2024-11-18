
def main():
    tekst=str(input("Podaj dane: "))
    print(zbiory(tekst))

def zbiory(dane):

    dane=dane.strip()

    if("+"in dane or "-" in dane or "*" in dane):
        if (dane[0]=="{" and dane[-1]=="}"):
            if("+" in dane):
                zbiory=dane.split("+")
                if(len(zbiory)!=2):
                    return "nieprawidlowa skladnia"

                zbior1=zbiory[0]
                zbior2=zbiory[1]
                zbior1=zbior1.replace("{","").replace("}","")
                zbior2=zbior2.replace("{","").replace("}","")
                zbior1=zbior1.split(",")
                zbior2=zbior2.split(",")
                return "wynik: ",str(set(zbior1).union(set(zbior2)))
            elif("-" in dane):
                zbiory=dane.split("-")
                if(len(zbiory)!=2):
                    return "nieprawidlowa skladnia"
                zbior1=zbiory[0]
                zbior2=zbiory[1]
                zbior1=zbior1.replace("{","").replace("}","")
                zbior2=zbior2.replace("{","").replace("}","")
                zbior1=zbior1.split(",")
                zbior2=zbior2.split(",")
                return "wynik: ",str(set(zbior1).difference(set(zbior2)))
            elif("*" in dane):
                zbiory=dane.split("*")
                if(len(zbiory)!=2):
                    return "nieprawidlowa skladnia"
                zbior1=zbiory[0]
                zbior2=zbiory[1]
                zbior1=zbior1.replace("{","").replace("}","")
                zbior2=zbior2.replace("{","").replace("}","")
                zbior1=zbior1.split(",")
                zbior2=zbior2.split(",")
                return "wynik: ",str(set(zbior1).intersection(set(zbior2)))
            

        else:
            return "nieprawidlowa skladnia"
    else:
        return "nieprawidlowy operator"

if __name__=="__main__":
    main()