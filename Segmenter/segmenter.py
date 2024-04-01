import re

class Segmenter:

    def zatBod(self,text):
        """Segmentuje vety, ktoré sú zakončené bodkov a nasleduje za nimi znak pravej zátvorky, medzera a nová veta."""
        text = re.sub(r'(?<=(\.\)))\s(?=[A-ZÁČĎÉÍŇÓŠŤÚÝ]+)', '\n', text)
        return text

    def triBod(self,text):
        """Segmentuje vety, ktoré sú zakončené znakom troch bodiek … a nasleduje za nimi nová veta"""
        text = re.sub(r'(?<=(…))\s(?=[A-ZÁČĎÉÍŇÓŠŤÚÝŽ])', '\n', text)
        return text

    def triBodSkrat(self,text):
        """Označuje tri bodky, ktoré nanaznačujú koniec vety znakom ∯"""
        text = re.sub(r'(?<=(\.\.))\.(?=\s[a-záčďéíňóšťúýžäô])', '∯', text)
        return text

    def listItemDvojBod(self,text):
        """Segmentuje číslovaný zoznam dĺžky 1-2 zakončený : a nasledujúci novou vetou"""
        text = re.sub(r'\s(?=(\d{1,2}\:\s([A-ZÁČĎÉÍŇÓŠŤÚÝŽ]|\d)))', '\n', text)
        return text

    def listItemZatv(self,text):
        """Segmentuje číslovaný zoznam dĺžky 1-2 zakončený ) a nasledujúci novou vetou"""
        text = re.sub(r'\s(?=(\d|\d{1,2}|[a-z])\)\s[A-ZÁČĎÉÍŇÓŠŤÚÝŽ])', '\n', text)
        return text

    def tabTriBod(self,text):
        """Segmentuje hranice vety, za ktorými nasledujú znaky tabulátora ···"""
        text = re.sub(r'(?<=(\.|\!|\?))\s(?=\·\·\·)', '\n', text)
        return text

    # SPISOVNA PRIAMA REC


    def pRKOt(self,text):
        """Segmentuje hranicu vety medzi priamou rečou zakončenou otáznikom a znakom úvodzoviek a novou vetou"""
        text = re.sub(r'(?<=(\?[\‘|\`|\'|\"]))\s(?=[A-ZÁČĎÉÍŇÓŠŤÚÝŽ]+)', '\n', text)
        return text

    def pRKVy(self,text):
        """Segmentuje hranicu vety medzi priamou rečou zakončenou výkričníkom a znakom úvodzoviek a novou vetou"""
        text = re.sub(r'(?<=(\![\‘|\`|\'|\"]))\s(?=[A-ZÁČĎÉÍŇÓŠŤÚÝŽ]+)', '\n', text)
        return text

    def pRKBod(self,text):
        """Segmentuje hranicu vety medzi priamou rečou zakončenou bodkou a znakom úvodzoviek a novou vetou"""
        text = re.sub(r'(?<=(\.[\‘|\`|\'|\"]))\s(?=[A-ZÁČĎÉÍŇÓŠŤÚÝŽ]+)', '\n', text)
        return text

    def pRKOtSpis(self,text):
        """Nahradzuje otáznik na konci priamej reči, za ktorou nasleduje uvádzacia veta, znakom ∀"""
        text = re.sub(r'(?<=[a-záčďéíňóšťúýžäô])\?(?=\s[a-záčďéíňóšťúýžäô]+)', '∀', text)
        return text

    def pRKVySpis(self,text):
        """Nahradzuje výkričník na konci priamej reči, za ktorou nasleduje uvádzacia veta, znakom ∁"""
        text = re.sub(r'(?<=[a-záčďéíňóšťúýžäô])\!(?=\s[a-záčďéíňóšťúýžäô]+)', '∁', text)
        return text

    # PORADOVE CISLA

    def porCis(self,text):
        """Nahradzuje bodku za poradovými číslami znakom ∯"""
        text = re.sub(r'(?<=\d)\.(?=\s(([a-záčďéíňóšťúýžäô])|\d))', '∯', text)
        return text

    def porCisRimJed(self,text):
        """Nahradzuje bodku za rímskymi poradovými číslami znakom ∯"""
        text = re.sub(r'(?<=[VXI])\.(?=\s([a-záčďéíňóšťúýžäô]|\d|\())', '∯', text)
        return text

    # PISMENNE SKRATKY

    def skratVelJedMale(self,text):
        """Nahradzuje bodku za skratkami zložených z veľkého a malého písmena nasledujúcimi veľkým písmenom znakom ∯"""
        text = re.sub(r'(?<=([A-Z][a-z]))\.(?=\s[A-ZÁČĎÉÍŇÓŠŤÚÝŽ]+)', '∯', text)
        return text

    def skratVel(self,text):
        """Nahradzuje bodku za skratkami zložených z jedného veľkého písmena znakom ∯"""
        text = re.sub(r'(?<=((\s|\.)[A-Z]))\.(?=\s([A-ZÀ-Ža-ž]|\d))', '∯', text)
        return text

    def skratTriMale(self,text):
        """Nahradzuje bodku za skratkami zložených z troch malých písmen nasledujúcimi malým písmenom znakom ∯"""
        text = re.sub(r'(?<=\s[a-záčďéíňóšťúýžäô]{3})\.(?=\s([a-záčďéíňóšťúýžäô]|\d))', '∯', text)
        return text

    def skratJedMale(self,text):
        """Nahradzuje bodku za skratkami zložených z jedného malého písmena nasledujúcimi malým písmenom znakom ∯"""
        text = re.sub(r'(?<=\s[a-záčďéíňóšťúýžäô])\.(?=\s([a-záčďéíňóšťúýžäô]|\d))', '∯', text)
        return text

    def skratVytiahnuteJedMale(self,text):
        """Nahradzuje bodku za vybranými skratkami zložených z jedného malého písmena znakom ∯"""
        text = re.sub(r'(?<=(\s|\(|\.)(t|j|r|č|c|s))\.(?=\s([A-Za-z]|\d))', '∯', text)
        return text

    def skratVytiahnuteDvaMale(self,text):
        """Nahradzuje bodku za vybranými skratkami zložených z dvoch malých písmen znakom ∯"""
        text = re.sub(r'(?<=(\s|\(|\.)(al|vs|zv|sv))\.(?=\s([A-Za-z]|\d|\())', '∯', text)
        return text

    # def skratVytiahnuteTriMale(self,text):
    #     """Nahradzuje bodku za vybranými skratkami zložených z troch malých písmen znakom ∯"""
    #     text = re.sub(r'(?<=(\s|\(|\.)(al|vs|zv|sv))\.(?=\s([A-Za-z]|\d|\())', '∯', text)
    #     return text

    def skratVytiahnuteStyriMale(self,text):
        """Nahradzuje bodku za vybranými skratkami zložených zo štyroch malých písmen znakom ∯"""
        text = re.sub(r'(?<=(\s|\(|\.)(napr))\.(?=\s([a-záčďéíňóšťúýžäô]|\d|\())', '∯', text)
        return text

    def skratVytiahnuteTituly(self, text):
        """Nahradzuje bodku za vybranými titulmi znakom ∯"""
        text = re.sub(r'(?<=(\s|\(|\.)(prof))\.(?=\s([A-ZÁČĎÉÍŇÓŠŤÚÝŽ]|\d|\())', '∯', text)
        return text

    def symbolOt(self,text):
        """Nahradzuje znak ∀ znakom ?"""
        text = re.sub(r'∀', '?', text)
        return text

    def symbolVy(self,text):
        """Nahradzuje znak ∁ znakom !"""
        text = re.sub(r'∁', '!', text)
        return text

    def symbol(self,text):
        """Nahradzuje znak ∯ znakom ."""
        text = re.sub(r'∯', '.', text)
        return text


    def final(self,text):
        """Segmentuje vety, ktoré sú zakončené ., ?, !, za ktorými hneď nasleduje znak medzery"""
        text = re.sub(r'(?<=(\.|!|\?))\s', '\n', text)
        return text

    def replaceSkrat(self,text):
        text = self.porCis(text)
        text = self.porCisRimJed(text)
        text = self.skratVelJedMale(text)
        text = self.skratVel(text)
        text = self.skratTriMale(text)
        text = self.skratVytiahnuteJedMale(text)
        text = self.skratVytiahnuteDvaMale(text)
        text = self.skratVytiahnuteStyriMale(text)
        text = self.skratJedMale(text)
        text = self.triBodSkrat(text)
        text = self.triBod(text)
        text = self.pRKOtSpis(text)
        text = self.pRKVySpis(text)
        text = self.final(text)
        text = self.zatBod(text)
        text = self.listItemDvojBod(text)
        text = self.listItemZatv(text)
        text = self.tabTriBod(text)
        text = self.pRKOt(text)
        text = self.pRKVy(text)
        text = self.pRKBod(text)
        text = self.symbol(text)
        text = self.symbolOt(text)
        text = self.symbolVy(text)
        return text

