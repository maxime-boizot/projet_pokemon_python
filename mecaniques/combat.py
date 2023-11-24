from classes import Dresseur, Equipe, Pokemon
from functions import prompting

Red = Dresseur("Red", 300, 20, 10, 10, Equipe([Pokemon("Dracofoutre", 100, 10, 5, 10),Pokemon("Tiploufion", 100, 10, 5, 10)]))
Cynthia = Dresseur("Cynthia",300, 17, 8, 0, Equipe([Pokemon("Dracofeuj", 100, 10, 5, 10),Pokemon("Tiploufion", 100, 10, 5, 10)]))

def combat(dresseur1 : Dresseur, dresseur2 : Dresseur):

    PokemonActifRed = dresseur1.Equipe._MEMBRES[0]
    PokemonActifCynthia = dresseur2.Equipe._MEMBRES[0]

    while PokemonActifCynthia > 0 and PokemonActifRed._HP > 0:
        prompting(f"{PokemonActifRed} attaque {PokemonActifCynthia} !")
        PokemonActifCynthia -= PokemonActifRed._ATK
        prompting(f"{PokemonActifCynthia} a {PokemonActifCynthia} HP restants !")
        prompting(f"{PokemonActifCynthia} attaque {dresseur1._NOM} !")
        PokemonActifRed._HP -= dresseur2.Equipe._MEMBRES[0]._ATK
        prompting(f"{dresseur1._NOM} a {PokemonActifRed._HP} HP restants !")
    if PokemonActifCynthia <= 0:
        prompting(f"{PokemonActifCynthia} a perdu !")
    elif PokemonActifRed._HP <= 0:
        prompting(f"{dresseur1._NOM} a perdu !")

combat()