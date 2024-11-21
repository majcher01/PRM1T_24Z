def dodawanie(a,b):
    assert isinstance(a, int) and isinstance(b,int), "niepoprawne dane"
    return a+b

def odejmowanie(a,b):
    assert isinstance(a, int) and isinstance(b,int), "niepoprawne dane"
    return a-b

def mnozenie(a,b):
    assert isinstance(a, int) and isinstance(b,int),"niepoprawne dane"
    return a*b

def dzielenie(a,b):
    assert isinstance(a, int) and isinstance(b,int),"niepoprawne dane"
    return a/b


if __name__ =="__main__":
    print("bardzo wazna operacja print")