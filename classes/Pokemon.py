from Entite import Entite

class Pokemon(Entite):
    def __init__(self, name: str, maxhealth: int, strength: int, defense: int, speed: int):
        super().__init__(name, maxhealth, strength, defense, speed)

    def __str__(self):
        return f"""{self._NOM}: 
    {self._HP}/{self._MAXHP} HP
    {self._ATK} ATK
    {self._DEF} DEF
    {self._VIT} VIT"""

    def get_atk(self):
        return self._ATK

    def set_atk(self, new_atk):
        self._ATK = new_atk

    def get_def(self):
        return self._DEF

    def set_def(self, new_def):
        self._DEF = new_def
    
    def get_name(self):
        print(self._NOM)
    
    def set_name(self):
        print(self._NOM)

if __name__ == "__main__":
    Dracofoutre = Pokemon("Dracofoutre", 100, 10, 5, 10)
            

