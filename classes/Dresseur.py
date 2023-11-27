from Entite import Entite
from Equipe import Equipe
from Pokemon import Pokemon

class Dresseur(Entite):
    def __init__(self, name :str, maxhealth : int, strength : int, defense :int, speed : int, team : Equipe):
        super().__init__(name, maxhealth, strength, defense, speed)
        self._EKIP = team
  
    
    def __str__(self):
        return  f"""{self._NOM} : 
    {self._HP}/{self._MAXHP} HP
    {self._ATK} ATK
    {self._DEF} DEF\n
    ---------------------------------------\n
    {self._EKIP}"""
            
            
    
if __name__ == "__main__":
    Cynthia = Dresseur("Cynthia",300, 17, 8, 0, team = Equipe([Pokemon("Dracofoutre", 100, 10, 5, 10),Pokemon("Tiploufion", 100, 10, 5, 10)]))
    print(Cynthia)
        
    pass