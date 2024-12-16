from zadanie1 import Koder


dict_encode = {'a': 'j', 'ą': 'k', 'b': 'l',
 'c': 'ł', 'ć': 'm', 'd': 'n', 'e': 'ń', 'ę': 'o', 'f': 'ó',
 'g': 'p', 'h': 'r', 'i': 's', 'j': 'ś', 'k': 't', 'l': 'u',
 'ł': 'w', 'm': 'x', 'n': 'y', 'ń': 'z', 'o': 'ź', 'ó': 'ż',
 'p': 'a', 'r': 'ą', 's': 'b', 'ś': 'c', 't': 'ć', 'u': 'd',
 'w': 'e', 'x': 'ę', 'y': 'f', 'z': 'g', 'ź': 'h', 'ż': 'i',
 '.':'.', ' ':' ', ',':','
 }

if __name__ =="__main__":


    """
    x=Koder(dict_encode)

    print(x.zakoduj(["a","b","c","1"]))

    print(x.odkoduj(["j","l","ł","1"]))
    """

    a="""
    Wybierz tryb:
    [1] - Kodowanie
    [2] - Odkodowywanie
    [3] - Statystyki

    """

    x=Koder(dict_encode)
    try:
        x.zakoduj("123")
    except Exception as e:
        print(e)

    try:
        x.odkoduj("123")
    except Exception as e:
        print(e)

    tryb=int(input(a))
    tekst=str(input("Podaj znaki oddzielone spacja: "))
    t2=list(tekst)


    match tryb:
        case 1:

            try:
                zakodowane=x.zakoduj(t2)
            except Exception as e:
                print(e)
            else:
                print(f"Wynik = {zakodowane}")

        case 2:
            try:
                odkodowane=x.odkoduj(t2)
            except ZnakNieWSlowniku as b:
                print(b)
            except Exception as e:
                print(e)
            else:
                print(f"Wynik = {odkodowane}")
        
        case 3:
            print(x.statystyki(t2))

        case _:
            print("Nieznany tryb!")
    print("""
    *********************
    *   WESOLYCH SWIAT  *
    *********************

    """)
