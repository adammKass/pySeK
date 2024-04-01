import unittest

import segmenter


class TestSegmenter(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.seg = segmenter.Segmenter()


#OSTATNÉ

    def test_zatBod(self):
        self.assertEqual(self.seg.zatBod("(text v zátvorke.) Toto bol text v zátvorke."), "(text v zátvorke.)\nToto bol text v zátvorke.")

    def test_triBod(self):
        self.assertEqual(self.seg.triBod("Ovocie, zelenina… To všetko tam bolo."), "Ovocie, zelenina…\nTo všetko tam bolo.")

    def test_triBod(self):
        self.assertEqual(self.seg.triBodSkrat("Ovocie, zelenina... a ešte viac."), "Ovocie, zelenina..∯ a ešte viac.")
        self.assertEqual(self.seg.triBodSkrat("Ovocie, zelenina... Ešte viac."), "Ovocie, zelenina... Ešte viac.")

    def test_listItemDvojBod(self):
        self.assertEqual(self.seg.listItemDvojBod(" 1: Toto je veta."), "\n1: Toto je veta.")

    def test_listItemZatv(self):
        self.assertEqual(self.seg.listItemZatv(" a) Toto je veta."), "\na) Toto je veta.")
        self.assertEqual(self.seg.listItemZatv(" 1) Toto je veta."), "\n1) Toto je veta.")
        self.assertEqual(self.seg.listItemZatv(" 12) Toto je veta."), "\n12) Toto je veta.")

    def test_tabTriBod(self):
        self.assertEqual(self.seg.tabTriBod("Toto je veta. ··· Ďalšia veta."), "Toto je veta.\n··· Ďalšia veta.")

# PRIAMA REČ

    def test_pRKOt(self):
        self.assertEqual(self.seg.pRKOt("'Kto to bol?' Opýtala sa."), "'Kto to bol?'\nOpýtala sa.")
        self.assertEqual(self.seg.pRKOt("`Kto to bol?` Opýtala sa."), "`Kto to bol?`\nOpýtala sa.")

    def test_pRKVy(self):
        self.assertEqual(self.seg.pRKVy("'Bol to on!' Vykríkla."), "'Bol to on!'\nVykríkla.")
        self.assertEqual(self.seg.pRKVy("`Bol to on!` Vykríkla."), "`Bol to on!`\nVykríkla.")

    def test_pRKBod(self):
        self.assertEqual(self.seg.pRKBod("'Bol to on.' Povedala."), "'Bol to on.'\nPovedala.")
        self.assertEqual(self.seg.pRKBod("`Bol to on.` Povedala."), "`Bol to on.`\nPovedala.")

    def test_pRKOtSpis(self):
        self.assertEqual(self.seg.pRKOtSpis("Kto to bol? opýtala sa."), "Kto to bol∀ opýtala sa.")

    def test_pRKVySpis(self):
        self.assertEqual(self.seg.pRKVySpis("Bol to on! vykríkla."), "Bol to on∁ vykríkla.")

# PORADOVÉ ČÍSLA

    def test_porCis(self):
        self.assertEqual(self.seg.porCis("Narodil sa 3. 4. 2002."), "Narodil sa 3∯ 4∯ 2002.")
        self.assertEqual(self.seg.porCis("Narodil sa 3. apríla."), "Narodil sa 3∯ apríla.")
        self.assertEqual(self.seg.porCis("Dobehol 3. Teda posledný."), "Dobehol 3. Teda posledný.")

    def test_porCisRimJed(self):
        self.assertEqual(self.seg.porCisRimJed("Karol IV. založil Karlovu univerzitu."), "Karol IV∯ založil Karlovu univerzitu.")
        self.assertEqual(self.seg.porCisRimJed("Volal sa Karol IV. Založil Karlovu univerzitu."), "Volal sa Karol IV. Založil Karlovu univerzitu.")

# SKRATKY

    def test_skratVelJedMale(self):
        self.assertEqual(self.seg.skratVelJedMale("Dom je na ulici St. Marca."), "Dom je na ulici St∯ Marca.")

    def test_skratVel(self):
        self.assertEqual(self.seg.skratVel("Človek A. K. sa narodil v apríli."), "Človek A∯ K∯ sa narodil v apríli.")

    def test_skratJedMale(self):
        self.assertEqual(self.seg.skratJedMale("Ukážka je na s. 23."), "Ukážka je na s∯ 23.")
        self.assertEqual(self.seg.skratJedMale("Je to na strane č. dvadsať."), "Je to na strane č∯ dvadsať.")
        self.assertEqual(self.seg.skratJedMale("Je to na piatej s. Je to tam."), "Je to na piatej s. Je to tam.")

    def test_skratTriMale(self):
        self.assertEqual(self.seg.skratTriMale("V treťom str. sa narodil."), "V treťom str∯ sa narodil.")
        self.assertEqual(self.seg.skratTriMale("Narodil sa v treťom str. Bolo to ráno."), "Narodil sa v treťom str. Bolo to ráno.")

    def test_skratVytiahnuteJedMale(self):
        self.assertEqual(self.seg.skratVytiahnuteJedMale("Ukážka je na s. 23."), "Ukážka je na s∯ 23.")

    def test_skratVytiahnuteDvaMale(self):
        self.assertEqual(self.seg.skratVytiahnuteDvaMale("Chrám sv. Víta."), "Chrám sv∯ Víta.")

    def test_skratVytiahnuteTriMale(self):
        self.assertEqual(self.seg.skratVytiahnuteTriMale("Chrám sv. Víta."), "Chrám sv∯ Víta.")

    def test_skratVytiahnuteStyriMale(self):
        self.assertEqual(self.seg.skratVytiahnuteStyriMale("Je to napr. pes."), "Je to napr∯ pes.")

    def test_skratVytiahnuteTituly(self):
        self.assertEqual(self.seg.skratVytiahnuteTituly("Je to prof. Malý."), "Je to prof∯ Malý.")


# NAHRÁDZANIE SYMBOLOV


    def test_symbolOt(self):
        self.assertEqual(self.seg.symbolOt("Kto to bol∀ opýtala sa."), "Kto to bol? opýtala sa.")

    def test_symbolVy(self):
        self.assertEqual(self.seg.symbolVy("Pozor∁ vykríkla."), "Pozor! vykríkla.")

    def test_symbol(self):
        self.assertEqual(self.seg.symbol("Je to prof∯ Malý."), "Je to prof. Malý.")

    def test_final(self):
        self.assertEqual(self.seg.final("Volal sa Peter. Mal 18."), "Volal sa Peter.\nMal 18.")
        self.assertEqual(self.seg.final("A.K. sa narodil 27. decembra."), "A.K.\nsa narodil 27.\ndecembra.")




if __name__ == '__main__':
    unittest.main()
