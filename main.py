from mecaniques.combat import combat
from classes.Pokemon import Pokemon
from classes.Dresseur import Dresseur
from classes.Equipe import Equipe
from classes.Entite import Entite

Red = Dresseur("Red", 300, 20, 10, 10, Equipe([Pokemon("Dracofeu", 100, 10, 5, 10),Pokemon("Spectrum", 100, 10, 5, 10)]))
Cynthia = Dresseur("Cynthia",300, 17, 8, 0, Equipe([Pokemon("Dracolosse", 100, 10, 5, 10),Pokemon("Tiplouf", 100, 10, 5, 10)]))

combat(Red, Cynthia)