morse_code = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..' }



def zakoduj(tekst):
    tekst=list(tekst)
    wynik=[]
    for i in tekst:
        if i in morse_code:
            wynik.append(morse_code[i])
        else:
            wynik.append("??")
    return wynik



def test(tekst):
    wynik=zakoduj(tekst)
    print(tekst,end=":\t")

    for i in wynik:
        print(i, end=" ")

test("SOS9")