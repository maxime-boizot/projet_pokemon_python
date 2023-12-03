from mecaniques.combat import combat
from mecaniques.lastfight import lastfight
from functions.prompting import clear_screen
from functions.prompting import prompting
from classes.Pokemon import Pokemon
from classes.Dresseur import Dresseur
from classes.Equipe import Equipe
from classes.Entite import Entite
from lore.cynthiaLines import *
from lore.lore import *
from lore.interactionsLines import *
import time


Red = Dresseur("Red", 300, 20, 10, 10, Equipe([Pokemon("Dracofeu", 111, 20, 5, 10),Pokemon("Spectrum", 77, 14, 7, 22), Pokemon("Pikachu", 66, 11, 11, 30), Pokemon("Pingoléon", 90, 16, 7, 17), Pokemon("Gardevoir", 77, 12, 2, 10)]))
Cynthia = Dresseur("Cynthia",130, 15, 8, 0, Equipe([Pokemon("Torterra", 83, 12, 3, 8),Pokemon("Leviathor", 44, 10, 2, 10),Pokemon("Togekiss", 104, 9, 6, 8),Pokemon("Luxray", 68, 12, 4, 30),Pokemon("Lucario", 72, 11, 2, 8),]))

clear_screen()
print(pokemon_logo)
time.sleep(3)
clear_screen()

time.sleep(1)
prompting(lore1)
time.sleep(1)
prompting(lore2)

time.sleep(3)
clear_screen()
prompting(lore3)

time.sleep(2)
clear_screen()
prompting("Cynthia :\n")
prompting(startDial)
time.sleep(1)
prompting(startDial2)
time.sleep(1)
prompting(startDial3)

time.sleep(1)
clear_screen()

prompting(initCombat)
time.sleep(1)
clear_screen()

prompting("Cynthia a choisi Bulbizarre !\n")
time.sleep(1)

combat(Red, Cynthia, 0)
lastfight(Red, Cynthia)