import sys, os

if(len(sys.argv)<3):
    exit("Podaj nazwy dwoch plikow!")

if(not os.path.exists(sys.argv[1]) or not os.path.exists(sys.argv[2])):
    exit("Podane pliki nie istnieja!")

plik1=open(sys.argv[1],"r")
plik2=open(sys.argv[2],"r")

zawartosc1=plik1.read()
zawartosc2=plik2.read()

zawartosc1=zawartosc1.strip()
zawartosc1=zawartosc1.split(" ")

zawartosc2=zawartosc2.strip()
zawartosc2=zawartosc2.split(" ")

for i in range (0,len(zawartosc1)):
    zawartosc1[i]=int(zawartosc1[i])

for i in range (0,len(zawartosc2)):
    zawartosc2[i]=int(zawartosc2[i])

print(f"""
Plik1 ({sys.argv[1]}):
Ilosc liczb: {len(zawartosc1)}
Suma liczb: {sum(zawartosc1)}
Srednia arytmetyczna: {sum(zawartosc1)/len(zawartosc1)}
\n
Plik2 ({sys.argv[2]}):
Ilosc liczb: {len(zawartosc2)}
Suma liczb: {sum(zawartosc2)}
Srednia arytmetyczna: {sum(zawartosc2)/len(zawartosc2)}
"""
)