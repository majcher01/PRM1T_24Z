import sys

def funkcja(nazwapliku):
    linie=[]
    with open(nazwapliku,"r") as file:
        for i in file:
            i=i.strip()
            linie.append(i)
    studenci={}
    for i in linie:
        n=i.split(",")
        studenci[n[2]]={
            "imię":n[0],
            "nazwisko":n[1],
            "oceny":n[3::]
        }


    return studenci

def nowafunkcja(slownik, nazwapliku):
    wynik=[]
    for i in slownik:
        oceny=slownik[i]["oceny"]
        for l in range(len(oceny)):
            oceny[l]=int(oceny[l])
        srednia=sum(oceny)/len(oceny)
        srednia=round(srednia,2)
        wynik.append([i,srednia])
    plik=open(nazwapliku,"w")
    for i in wynik:
        plik.write(str(i[0])+" "+str(i[1])+"\n")
    plik.close()


if  __name__=="__main__":
    if(len(sys.argv)>2):
        wejsciowy=sys.argv[1]
        wyjsciowy=sys.argv[2]
        nowafunkcja(funkcja(wejsciowy),wyjsciowy)
    else:
        exit(print("Brak argumentow!"))