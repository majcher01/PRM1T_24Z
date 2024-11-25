import math

def calka(funkcja,xp,xk,n,metoda):
    xp=int(xp)
    xk=int(xk)
    n=int(n)
    if("cos" in funkcja):
        funkcja=funkcja.replace("cos(x)","math.cos(x)")
    if(metoda=="met1"):
        punkty_przedzialu=[]
        for i in range(1,(n+1)):
            temp=xp+(i/n)*(xk-xp)
            punkty_przedzialu.append(temp)
        
        odleglosc_miedzy_punktami=(xk-xp)/n

        wartosc_funkcji_w_punktach=[]
        for i in range(0,n):
            wyrazenie=funkcja.replace("x",str(punkty_przedzialu[i]))
            wartosc_funkcji_w_punktach.append(eval(wyrazenie))

        suma_iloczynow=odleglosc_miedzy_punktami*sum(wartosc_funkcji_w_punktach)
        
        return suma_iloczynow
    elif(metoda=="met2"):
        punkty_przedzialu=[]
        for i in range(0,(n+1)):
            temp=xp+(i/n)*(xk-xp)
            punkty_przedzialu.append(temp)
        
        odleglosc_miedzy_punktami=(xk-xp)/n

        wartosc_funkcji_w_punktach=[]

        for i in range(0,n):
            wyrazenie=funkcja.replace("x",str(punkty_przedzialu[i]))
            wartosc_funkcji_w_punktach.append(eval(wyrazenie))

        suma=sum(wartosc_funkcji_w_punktach)
        return suma
        


with open("dane.in","r") as dane:
    for linia in dane:
        linia=linia.strip()
        dane=linia.split("\t")
        print(calka(dane[0],dane[1],dane[2],dane[3],dane[4]))




#print(calka("x**2+5","-1","1",10,"met2"))

