def main():

    str1 = 'Lorem ipsum dolor sit amet, Consectetur adipiscing elit. Curabitur vel ante lobortis, elementum justo sed, ornare tortor. Integer volutpat ullamcorper lorem vitae aliquet. Cras ligula dolor, elementum sit amet varius a, suscipit et lacus. Ut risus dolor, consequat at semper non, facilisis ut elit. Aliquam vel ipsum vel urna ornare mattis id sed ligula. Nam et odio suscipit, feugiat est vel, mattis nunc. Donec ullamcorper ligula velit, sit amet varius odio posuere eu. Nunc interdum, leo ut laoreet tincidunt, est risus egestas libero, vel vestibulum magna dolor sed turpis. In pulvinar erat sollicitudin magna convallis varius. Pellentesque a velit lectus.'
    print(policz(str1))




def policz(tekst):
    duze=[]
    for i in tekst:
        if(i.isupper()):
            duze.append(i)
    bez_duplikatow=set(duze)
    wynik={}

    for i in sorted(bez_duplikatow):
        wynik[i]=(duze.count(i)/len(duze))
    
    return wynik

if __name__=="__main__":
    main()