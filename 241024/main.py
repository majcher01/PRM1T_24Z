wiek = int(input("Podaj wiek: "))

z_dziecieca = {
    "ulga": 0.3,
    "opis_ulgi": "Ulga dla dzieci ponizej 10 lat - 30% ceny",
    "wiek_dol": 0,
    "wiek_gora": 10,
}

z_mlodziez = {
    "ulga": 0.5,
    "opis_ulgi": "Ulga dla mlodziezy i studentow ponizej 26 lat - 50%",
    "wiek_dol": 10,
    "wiek_gora": 26,
}

z_normalna = {"ulga": 1, "opis_ulgi": "Bilet normalny", "wiek_dol": 26, "wiek_gora": 60}

z_senior = {
    "ulga": 0.7,
    "opis_ulgi": "Ulga dla seniorow powyzej 60 lat - 70%",
    "wiek_dol": 60,
    "wiek_gora": 200,
}


znizki = [z_dziecieca, z_mlodziez, z_normalna, z_senior]


def przydziel_znizke(wiek, znizki):
    for i in znizki:
        if i["wiek_dol"] < wiek <= i["wiek_gora"]:
            print(i["opis_ulgi"])
            break


przydziel_znizke(wiek, znizki)

if input("wyswietlic wszystkie znizki? (t/n)") == "t":
    for i in znizki:
        print(i["opis_ulgi"])
