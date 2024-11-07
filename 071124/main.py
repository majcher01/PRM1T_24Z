imiona=["marcin","Anna","tomasz","an na","Justyna","RoMan ","MAr cin"]


for i in range(0,len(imiona)):
    imiona[i]=imiona[i].replace(" ","")

for i in range(0,len(imiona)):
    imiona[i]=imiona[i].lower()
    imiona[i]=imiona[i].replace(imiona[i][0],imiona[i][0].upper(),1)

imiona.sort()

for imie in imiona:
    print(imie,end=", ")

imiona2=set(imiona)

print("\n\n"+str(imiona2))


for imie in imiona2:
    if(imie[-1]=="a"):
        print(imie)
    else:
        continue