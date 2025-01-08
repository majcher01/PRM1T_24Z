import unittest
from klasa import TrzymamMaila




class TestCalculations(unittest.TestCase):


    def test_nazwa(this):
        x=TrzymamMaila("user1")
        this.assertEqual(x.nazwauzytkownika,"user1", "Nazwa uzytkownika niepoprawna!")

    def test_dodajadres(this):
        x=TrzymamMaila("user1")
        this.assertTrue(x.dodajadres("test@test.pl"))
        this.assertFalse(x.dodajadres("test@test.pl"))
        x.dodajadres("email1@email.pl")
        x.dodajadres("email2@email.pl")
        x.dodajadres("email3@email.pl")

        this.assertEqual(len(x.adresy["user1"]),4)

        with this.assertRaises(Exception):
            x.dodajadres("adres")
        with this.assertRaises(Exception):
            x.dodajadres("email@@.pl")
        with this.assertRaises(Exception):
            x.dodajadres("adres")
        with this.assertRaises(Exception):
            x.dodajadres("adr es")
        with this.assertRaises(Exception):
            x.dodajadres("adre\ns")
        with this.assertRaises(Exception):
            x.dodajadres("@adres@")
        with this.assertRaises(Exception):
            x.dodajadres("adres@")
        with this.assertRaises(Exception):
            x.dodajadres("adres.")

    def test_usunadres(this):
        x=TrzymamMaila("user1")
        x.dodajadres("email1@email.pl")
        x.dodajadres("email2@email.pl")
        x.dodajadres("email3@email.pl")

        this.assertTrue(x.usunadres("email1@email.pl"))
        this.assertFalse(x.usunadres("adres@adres.pl"))
        this.assertEqual(len(x.adresy["user1"]),2)

    def test_sort(this):
        x=TrzymamMaila("user1")
        this.assertFalse(x.sortuj())

        x.dodajadres("email1@email.pl")
        x.dodajadres("email2@email.pl")
        x.dodajadres("email3@email.pl")

        z=x.adresy["user1"]
        x.sortuj()

        this.assertEqual(z,x.adresy["user1"])
        






if __name__ == '__main__':
    unittest.main()