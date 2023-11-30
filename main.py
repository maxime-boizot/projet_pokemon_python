from mecaniques.combat import combat
from mecaniques.lastfight import lastfight
from classes.Pokemon import Pokemon
from classes.Dresseur import Dresseur
from classes.Equipe import Equipe
from classes.Entite import Entite


Red = Dresseur("Red", 300, 20, 10, 10, Equipe([Pokemon("Dracofeu", 100, 90, 5, 10),Pokemon("Spectrum", 60, 6, 3, 10), Pokemon("Pikachu", 35, 12, 10, 25), Pokemon("Pingoléon", 50, 8, 2, 10), Pokemon("Gardevoir", 50, 8, 2, 10)]))
Cynthia = Dresseur("Cynthia",300, 17, 8, 0, Equipe([Pokemon("Bulbizarre", 10, 5, 3, 8),Pokemon("Tiplouf", 20, 8, 2, 10)]))

combat(Red, Cynthia, 0)
lastfight(Red, Cynthia)