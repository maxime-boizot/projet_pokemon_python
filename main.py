from mecaniques.combat import combat
from classes.Pokemon import Pokemon
from classes.Dresseur import Dresseur
from classes.Equipe import Equipe
from classes.Entite import Entite

Team = Equipe([Pokemon("Dracofoutre", 100, 10, 5, 10),Pokemon("Tiploufion", 100, 10, 5, 10),Pokemon("Pikachu", 35, 12, 10, 25)])

Red = Dresseur("Red", 300, 20, 10, 10, Team)
Cynthia = Dresseur("Cynthia",300, 17, 8, 0, Equipe([("Dracofoutre", 60, 13, 2, 10),Pokemon("Pikachu", 65, 12, 7, 25)]))

combat(Red, Cynthia)