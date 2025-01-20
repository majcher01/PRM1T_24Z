import numpy as np
import sys
import matplotlib.pyplot as plt

def wczytajdane(nazwa):

    try:
        xp,yp1,yp2,yp3,yp4,yp5=np.loadtxt(nazwa, unpack=True)
    except:
        raise Exception("Blad odczytu pliku")
    return xp,yp1,yp2,yp3,yp4,yp5


def rysuj(x,y,styles,markers,filename):
    for i in range(len(y)):
        plt.plot(x,y[i],linestyle=styles[i],marker=markers[i])

    plt.xlabel("Os X")
    plt.ylabel("Os Y")
    plt.title("Wykres")
    plt.grid()
    try:
        plt.savefig(filename)
        plt.show()
    except:
        raise Exception("Blad zapisu pliku")
        
if __name__=="__main__":
    try:
        nazwapliku=sys.argv[1]
    except:
        raise Exception("Nie podano nazwy pliku")
    xp,yp1,yp2,yp3,yp4,yp5=wczytajdane(nazwapliku)

    y=[yp1,yp2,yp3,yp4,yp5]
    try:
        nazwawykresu=sys.argv[2]
    except:
        raise Exception("Nie podano nazwy pliku wyjsciowego")
    styles=["solid","dashed","dashdot","dotted","solid"]
    markers=["o","*","X","P","s"]
    rysuj(xp,y,styles,markers,nazwawykresu)


