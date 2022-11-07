import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_negatiivinen_tilavuus_nollautuu(self):
        virheellinen_varasto = Varasto(-1)
        self.assertAlmostEqual(virheellinen_varasto.tilavuus,0)

    def test_negatiivinen_saldo_nollautuu(self):
        virheellinen_varasto = Varasto(10,-10)
        self.assertAlmostEqual(virheellinen_varasto.saldo,0)

    def test_ylitaysi_varasto_tyhjenee(self):
        ylitaysi_varasto = Varasto(5,10)
        self.assertAlmostEqual(ylitaysi_varasto.saldo,5)

    def test_tilavuus_ei_ylity_lisatessa(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_varastoon_ei_voi_lisata_negatiivista(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varasto_ei_lisatessa_mene_yli(self):
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ei_voi_ottaa_negatiivista(self):
        self.varasto.lisaa_varastoon(5)
        ota = self.varasto.ota_varastosta(-3)
        self.assertAlmostEqual(ota, 0)
    
    def test_saldon_yli_ottaminen_palauttaa_saldon(self):
        self.varasto.lisaa_varastoon(5)
        ota = self.varasto.ota_varastosta(9)
        self.assertAlmostEqual(ota, 5)
    
    def test_saldon_yli_ottaminen_tyhjentaa_varaston(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(9)
        self.assertAlmostEqual(self.varasto.saldo,0)
    
    def test_varasto_merkkijonona_tulostuu_oikein(self):
        self.assertEqual("saldo = 0, vielä tilaa 10",str(self.varasto))
