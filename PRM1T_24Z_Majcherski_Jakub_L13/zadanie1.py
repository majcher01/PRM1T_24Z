import numpy as np

def funkcja(n):

    if n<=0:
        raise Exception("nieprawidlowy n")
    e=np.e
    lista=np.arange(1,n+1)

    #"(1+1/n)^n"
    ciag=(1+1/lista)**lista

    roznica=e-ciag

    return ciag,roznica


def main():
    try:
        ciag,roznica=funkcja(4)
    except Exception as e:
        exit(print(e))

    for i in range(0,len(ciag)):
        print(f"Wynik: {ciag[i]}, roznica: {roznica[i]}")


if __name__=="__main__":
    main()
