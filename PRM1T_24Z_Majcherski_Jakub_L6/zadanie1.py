

def czypalindrom(tekst):
    tekst=tekst.lower()
    wyrazy=len(tekst.split(" "))

    for l in tekst:
        if(not l.isalpha()):
            tekst=tekst.replace(l,"")

    if(tekst==tekst[::-1]):
        return True,wyrazy
    else:
        return False,wyrazy


def main():
    print(czypalindrom("Jeż leje lwa, paw leje lżej"))
    print(czypalindrom("Madam I'm Adam"))

if __name__ == "__main__":
    main()

