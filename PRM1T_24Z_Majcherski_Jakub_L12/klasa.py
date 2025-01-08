import re

class TrzymamMaila:
    def __init__(this, nazwauzytkownika):
        this.adresy=dict()
        this.adresy[nazwauzytkownika]=[]
        this.nazwauzytkownika=nazwauzytkownika
    
    def dodajadres(this, adres):
        regex = r"^\S+@\S+\.\S+$"
        if(not re.match(regex, adres)):
            raise Exception("Niepoprawny adres!")

        if adres in this.adresy[this.nazwauzytkownika]:
            return False
        else:
            this.adresy[this.nazwauzytkownika].append(adres)
            return True

    def wyswietl(this, nazwauzytkownika):
        print(this.adresy[nazwauzytkownika])

    def usunadres(this,adres):
        if(not this.adresy[this.nazwauzytkownika] or adres not in this.adresy[this.nazwauzytkownika]):
            return False
        else:
            this.adresy[this.nazwauzytkownika].remove(adres)
            return True

    def sortuj(this):
        if(not this.adresy[this.nazwauzytkownika]):
            return False
        else:
            this.adresy[this.nazwauzytkownika].sort()
            return True



