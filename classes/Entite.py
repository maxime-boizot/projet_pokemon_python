from functions.prompting import prompting

class Entite:
    def __init__(self, name :str, maxhealth : int, strength : int, defense :int, speed : int):
        self._NOM = name
        self._MAXHP = maxhealth
        self._HP = maxhealth
        self._ATK = strength
        self._DEF = defense
        self._VIT = speed
    
    def __str__(self):
        return  f"""{self._NOM} : 
    {self._HP}/{self._MAXHP} HP
    {self._ATK} ATK
    {self._DEF} DEF
    {self._VIT} VIT"""
    
    def attack(self, target):
        if not self.is_alive():
            return
        damage = self._ATK - target._DEF
        if damage < 0:
            damage = 0
        target._HP -= damage
        prompting(f"{self._NOM} Attaque ! Il a fait {damage} dégats")
        
    def is_alive(self):
        return self._HP > 0
    
    def show_HPbar(self):
        healthbar = ""
        for _ in range(0, self._MAXHP):
            healthbar += " "
        for i in range(0, self._HP):
            healthbar = healthbar[:i] + "█" + healthbar[i+1:]
        print(f"{self._NOM} : [{healthbar}]")