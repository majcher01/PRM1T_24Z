l1=[1, 6, 6, 6, 6, 5, 2, 2, 4, 3]

def operacje(lista):
    print("Liczba elementow: "+str(len(lista)))
    #duplikaty
    licznik=0
    niepowtarzajacesie=[]
    for i in lista:
        if(lista.count(i)==1):
            licznik=licznik+1
            niepowtarzajacesie.append(i)
    print("Ilosc niepowtarzajacych sie elementow: "+str(licznik))
    print("Elementy: "+str(niepowtarzajacesie))
    #sortowanie
    lista.sort()

    #usuwanie duplikatow
    nowa=[]
    for i in lista:
        if (lista.count(i)==1):
            nowa.append(i)
    lista=nowa
    del nowa
    print("Lista bez duplikatow: "+str(lista))
    #usuniecie ostatniego
    lista.pop()
    print("Lista bez ostatniego"+str(lista))
    
    #dodanie na poczatku i koncu
    element=lista[-1]
    lista.append(element)
    lista.insert(0,element)
    print("Lista z dodanymi elementami"+str(lista))

    #sortowanie listy

    for i in range(0,(len(lista)-1)):
        if(i%2==0):
            el=lista[i]
            lista.pop(i)
            lista.insert(0,el)
        else:
            el=lista[i]
            lista.pop(i)
            lista.append(el)
    print("Lista odpowiednio posortowana"+str(lista))



operacje(l1)