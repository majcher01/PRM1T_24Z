from klasa import PhoneBook


def main():
    x=PhoneBook(1)
    x.add_record("user1","12345")
    x.add_record("user2","54321")

    y=PhoneBook(1)
    y.add_record("user3","44332")

    z=PhoneBook(1)
    z.add_record("user3","44332")

    x.show_records()
   #Zadanie 2 
    print(y)

    print(x==y)
    print(y==z)
    t=object()
    try:
        print(x==t)
    except:
        print("Wystapil blad!")

    print(x>y)
    print(y>x)


if __name__=="__main__":
    main()