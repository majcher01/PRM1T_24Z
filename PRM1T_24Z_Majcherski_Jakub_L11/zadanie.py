
class ZnakNieWSlowniku(Exception):
    def __init__(this, znak):
        this.message="Znak nie znajduje sie w slowniku"
        this.znak=znak

    def __str__(this):
        return f"{this.message}, znak={this.znak}"


class Koder:
    def __init__(this, slownik):
        this.slownik_do_kodowania=slownik
        this.slownik_do_odkodowania={value: key for key, value in this.slownik_do_kodowania.items()}

    def zakoduj(this, lista):
        if(not isinstance(lista, list)):
            raise Exception("Zmienna nie jest lista!")
        wynik=[]
        for i in lista:
            if(i not in this.slownik_do_kodowania):
                #raise Exception(f"Znak {i} nie znajduje sie w slowniku")
                raise ZnakNieWSlowniku(i)
            else:
                wynik.append(this.slownik_do_kodowania[i])

        return wynik

    def odkoduj(this,lista):
        if(not isinstance(lista, list)):
            raise Exception("Zmienna nie jest lista!")
        wynik=[]
        for i in lista:
            if(i not in this.slownik_do_odkodowania):
                #raise Exception(f"Znak {i} nie znajduje sie w slowniku")
                raise ZnakNieWSlowniku(i)
            else:
                wynik.append(this.slownik_do_odkodowania[i])
        return wynik


    def statystyki(this,tekst):
        pojedyncze=set(tekst)
        pojedyncze=sorted(pojedyncze)
        wynik=dict()
        for i in pojedyncze:
            a=tekst.count(i)
            wynik[i]=a
        return wynik
