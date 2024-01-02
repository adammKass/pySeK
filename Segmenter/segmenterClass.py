import re

class Segmenter:
    def __init__(self):
        self.name="mick"

    def zatBod(self,text):
        text = re.sub(r'\.\)\s(?=[A-ZÁČĎÉÍŇÓŠŤÚÝ]+)', '.)\n', text)
        return text

    def triBod(self,text):
        text = re.sub(r'(?<=(…))\s(?=[A-ZÁČĎÉÍŇÓŠŤÚÝŽ])', '\n', text)
        return text

    def triBodSkrat(self,text):
        text = re.sub(r'(?<=(\.\.))\.(?=\s[a-záčďéíňóšťúýžäô])', '∯', text)
        return text

    def listItemDvojBod(self,text):
        text = re.sub(r'\s(?=(\d{1,2}\:\s([A-ZÁČĎÉÍŇÓŠŤÚÝŽ]|\d)))', '\n', text)
        return text

    def listItemZatv(self,text):
        text = re.sub(r'\s(?=(\d|\d{1,2}|[a-z])\)\s[A-ZÁČĎÉÍŇÓŠŤÚÝŽ])', '\n', text)
        return text

    def tabTriBod(self,text):
        text = re.sub(r'(?<=(\.|\!|\?))\s(?=\·\·\·)', '\n', text)
        return text

    # SPISOVNA PRIAMA REC


    def pRKOt(self,text):
        text = re.sub(r'(?<=(\?[\‘|\`|\'|\"]))\s(?=[A-ZÁČĎÉÍŇÓŠŤÚÝŽ]+)', '\n', text)
        return text

    # def __pRKOt(self,text):
    #     text = re.sub(r'\?[\‘|\'|\"]\s(?=[A-ZÁČĎÉÍŇÓŠŤÚÝŽ]+)', '?‘\n', text)
    #     return text

    def pRKVy(self,text):
        text = re.sub(r'(?<=(\![\‘|\`|\'|\"]))\s(?=[A-ZÁČĎÉÍŇÓŠŤÚÝŽ]+)', '\n', text)
        return text

    def pRKBod(self,text):
        text = re.sub(r'(?<=(\.[\‘|\`|\'|\"]))\s(?=[A-ZÁČĎÉÍŇÓŠŤÚÝŽ]+)', '\n', text)
        return text

    def pRKOtSpis(self,text):
        text = re.sub(r'(?<=[a-záčďéíňóšťúýžäô])\?(?=\s[a-záčďéíňóšťúýžäô]+)', '∀', text)
        return text

    def pRKVySpis(self,text):
        text = re.sub(r'(?<=[a-záčďéíňóšťúýžäô])\!(?=\s[a-záčďéíňóšťúýžäô]+)', '∁', text)
        return text

    # PORADOVE CISLA

    def porCis(self,text):
        text = re.sub(r'(?<=\d)\.(?=\s(([a-záčďéíňóšťúýžäô])|\d))', '∯', text)
        return text

    def porCisRimJed(self,text):
        text = re.sub(r'(?<=[VXI])\.(?=\s([a-záčďéíňóšťúýžäô]|\d|\())', '∯', text)
        return text

    # PISMENNE SKRATKY

    def skratVelJedMale(self,text):
        text = re.sub(r'(?<=([A-Z][a-z]))\.(?=\s[A-ZÁČĎÉÍŇÓŠŤÚÝŽ]+)', '∯', text)
        return text

    def skratVel(self,text):
        text = re.sub(r'(?<=((\s|\.)[A-Z]))\.(?=\s([A-ZÀ-Ža-ž]|\d))', '∯', text)
        return text

    def skratTriMale(self,text):
        text = re.sub(r'(?<=\s[a-záčďéíňóšťúýžäô]{3})\.(?=\s([a-záčďéíňóšťúýžäô]|\d))', '∯', text)
        return text

    def skratJedMale(self,text):
        text = re.sub(r'(?<=\s[a-záčďéíňóšťúýžäô])\.(?=\s([a-záčďéíňóšťúýžäô]|\d))', '∯', text)
        return text

    def skratVytiahnuteJedMale(self,text):
        text = re.sub(r'(?<=(\s|\(|\.)(t|j|r|č|c|s))\.(?=\s([A-Za-z]|\d))', '∯', text)
        return text

    def skratVytiahnuteDvaMale(self,text):
        text = re.sub(r'(?<=(\s|\(|\.)(al|vs|zv|sv))\.(?=\s([A-Za-z]|\d|\())', '∯', text)
        return text

    def skratVytiahnuteTriMale(self,text):
        text = re.sub(r'(?<=(\s|\(|\.)(al|vs|zv|sv))\.(?=\s([A-Za-z]|\d|\())', '∯', text)
        return text

    def skratVytiahnuteStyriMale(self,text):
        text = re.sub(r'(?<=(\s|\(|\.)(napr))\.(?=\s([a-záčďéíňóšťúýžäô]|\d|\())', '∯', text)
        return text

    def skratVytiahnuteTituly(self, text):
        text = re.sub(r'(?<=(\s|\(|\.)(prof))\.(?=\s([A-ZÁČĎÉÍŇÓŠŤÚÝŽ]|\d|\())', '∯', text)
        return text

    def symbolOt(self,text):
        text = re.sub(r'∀', '?', text)
        return text

    def symbolVy(self,text):
        text = re.sub(r'∁', '!', text)
        return text

    def symbol(self,text):
        text = re.sub(r'∯', '.', text)
        return text


    def final(self,text):
        text = re.sub(r'(?<=(\.|!|\?))\s', '\n', text)
        return text

    def __perTest(self,text):
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

