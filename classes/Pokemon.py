from classes.Entite import Entite

class Pokemon(Entite):
    def __init__(self, name: str, maxhealth: int, strength: int, defense: int, speed: int):
        super().__init__(name, maxhealth, strength, defense, speed)

    def __str__(self):
        return f"""
    {self._NOM}: {self._HP}/{self._MAXHP} HP | {self._ATK} ATK | {self._DEF} DEF | {self._VIT} VIT
    """

    def __repr__(self):
        return self.__str__()

    def get_atk(self):
        return self._ATK

    def set_atk(self, new_atk):
        self._ATK = new_atk