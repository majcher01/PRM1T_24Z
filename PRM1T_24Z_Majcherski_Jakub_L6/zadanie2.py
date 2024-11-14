

def zamien(tekst,slownik):
    niema=[]
    for i in slownik:
        if(i in tekst):
            tekst=tekst.replace("<"+str(i)+">",str(slownik[i]))
        else:
            niema.append(i)
    if(len(niema)==0):
        return tekst
    else:
        mes="Nie znaleziono znaczników: "+str(niema)
        return tekst,mes


def main():
    tekst= "Nazywam się <imię> <nazwisko>, mam <wiek> lat."
    słownik= {"imię": "Jan", "nazwisko": "Kiepura", "wiek": 121}
    print(zamien(tekst,słownik))

    tekst2= "Nazywam się <imię> <nazwisko>, mam <wiek> lat."
    słownik2= {"imięx": "Jan", "nazwiskox": "Kiepura", "wiek": 121}
    print(zamien(tekst2,słownik2))

if __name__=="__main__":
    main()