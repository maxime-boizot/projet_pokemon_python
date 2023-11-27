from mecaniques.combat import combat
from classes.Pokemon import Pokemon
from classes.Dresseur import Dresseur
from classes.Equipe import Equipe
from classes.Entite import Entite


Red = Dresseur("Red", 300, 20, 10, 10, Equipe([Pokemon("Dracofeu", 100, 12, 5, 5),Pokemon("Spectrum", 60, 6, 3, 10), Pokemon("Pikachu", 35, 12, 10, 25), Pokemon("Pingoléon", 50, 8, 2, 10), Pokemon("Gardevoir", 50, 8, 2, 10)]))
Cynthia = Dresseur("Cynthia",300, 17, 8, 0, Equipe([Pokemon("Bulbizarre", 110, 60, 3, 8),Pokemon("Tiplouf", 50, 8, 2, 10)]))

combat(Red, Cynthia, 0)