class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        self.tilavuus = self.validate(tilavuus,tilavuus)
        self.saldo = self.validate(alku_saldo, tilavuus)

    # huom: ominaisuus voidaan myös laskea.
    # Ei tarvita erillistä kenttää viela_tilaa tms.

    def validate(self,value,max_value):
        if value >= 0:
            if value <= max_value:
                return value
            return max_value
        return 0

    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
