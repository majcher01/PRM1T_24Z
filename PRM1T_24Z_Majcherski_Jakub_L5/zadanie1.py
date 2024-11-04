import random
lista_ocen=[]

for i in range(0,30):
    lista_ocen.append(random.randint(0,5))

lista2=[]

for i in range(0,len(lista_ocen)):
    lista2.append((i,lista_ocen[i]))

print("Lista2: "+str(lista2)+"\n")


lista_ocen.sort()

print("Lista ocen posortowana "+str(lista_ocen)+"\n")

slownik=dict()
for i in range(6):
    slownik[i]=[]

for i in lista2:
    if(i[1]==0):
        slownik[0].append(i[0])
    elif(i[1]==1):
        slownik[1].append(i[0])
    elif(i[1]==2):
        slownik[2].append(i[0])
    elif(i[1]==3):
        slownik[3].append(i[0])
    elif(i[1]==4):
        slownik[4].append(i[0])
    elif(i[1]==5):
        slownik[5].append(i[0])

print("Konkretne oceny i indeksy: "+str(slownik)+"\n")

statystyki=dict()

for i in range(6):
    statystyki[i]=len(slownik[i])

print("Statystyki: "+str(statystyki)+"\n")

zaliczenie= {
    'zal':[],
    'nzal':[]
}

for i in range(3,6):
    for j in slownik[i]:
        zaliczenie['zal'].append(j)

for i in range(0,3):
    for j in slownik[i]:
        zaliczenie['nzal'].append(j)

print("Zalicznie: "+str(zaliczenie)+"\n")

def czyzaliczyl(indeksy):
    wynik=[]
    if isinstance(indeksy,list):
        for i in indeksy:
            if i in zaliczenie['zal']:
                wynik.append([i,"TAK"])
            else:
                wynik.append([i,"NIE"])
    else:
        if indeksy in zaliczenie['zal']:
            wynik.append([indeksy,"TAK"])
        else:
            wynik.append([indeksy,"NIE"])
    
    return wynik

print(czyzaliczyl([0,3,23,27]))
