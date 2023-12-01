from classes.Entite import Entite
from classes.Equipe import Equipe
from classes.Pokemon import Pokemon

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