import os,sys

def nazwairozmiar(katalog):
    pliki=os.listdir(katalog)
    zawartosc=[]

    for i in pliki:
        path=katalog+"/"+i
        if(not os.path.isfile(path)):
            continue
        zawartosc.append([i,str(os.stat(path).st_size)])
    return zawartosc

def dwakatalogi(kat1, kat2):
    zawartosc1=nazwairozmiar(kat1)
    zawartosc2=nazwairozmiar(kat2)
    #plikik2=os.listdir(kat2)

    sawobu=[]
    satylkow1=[]
    satylkow2=[]

    for i in range(len(zawartosc1)):
        if(zawartosc1[i] in zawartosc2):
            sawobu.append(zawartosc1[i])
        else:
            satylkow1.append(zawartosc1[i])
    for i in range(len(zawartosc2)):
        if(zawartosc2[i] in zawartosc1):
            sawobu.append(zawartosc2[i])
        else:
            satylkow2.append(zawartosc2[i])

    sawobubezduplikatow = list(set(tuple(sorted(sub)) for sub in sawobu))

    nazwaoba="sa_w_"+str(kat1)+"_i_w_"+str(kat2)+".txt"
    nazwasaw1="sa_tylko_w_"+str(kat1)+".txt"
    nazwasaw2="sa_tylko_w_"+str(kat2)+".txt"

    pliksawobu=open(nazwaoba,"w")
    pliksaw1=open(nazwasaw1,"w")
    pliksaw2=open(nazwasaw2,"w")

    for i in sawobubezduplikatow:
        pliksawobu.write(str(i[1])+" "+str(i[0])+"\n")

    for i in satylkow1:
        pliksaw1.write(str(i[0])+" "+str(i[1])+"\n")

    for i in satylkow2:
        pliksaw2.write(str(i[0])+" "+str(i[1])+"\n")

    pliksawobu.close()
    pliksaw1.close()
    pliksaw2.close()



#os.stat()
#nazwa=input("podaj nazwe: ")

#print(nazwairozmiar(nazwa))

if __name__=="__main__":
    if(len(sys.argv)>1):
        dwakatalogi(sys.argv[1],sys.argv[2])
    else:
        exit(print("Za malo argumentow!"))