from classes.Pokemon import Pokemon
from classes.Dresseur import Dresseur
from classes.Equipe import Equipe
from classes.Entite import Entite
from functions.prompting import prompting


def combat(dresseur1 : Dresseur, dresseur2 : Dresseur):

    PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
    PokemonActifCynthia = dresseur2._EKIP.get_equipe()[0]

    while PokemonActifCynthia._HP > 0 and PokemonActifRed._HP > 0:
        prompting(f"{PokemonActifRed} attaque {PokemonActifCynthia} !")
        PokemonActifCynthia._DEF -= PokemonActifRed._ATK
        prompting(f"{PokemonActifCynthia} a {PokemonActifCynthia} HP restants !")
        prompting(f"{PokemonActifCynthia} attaque {dresseur1._NOM} !")
        PokemonActifRed._HP -= dresseur2.Equipe._MEMBRES[0]._ATK
        prompting(f"{dresseur1._NOM} a {PokemonActifRed._HP} HP restants !")
    if PokemonActifCynthia <= 0:
        prompting(f"{PokemonActifCynthia} a perdu !")
    elif PokemonActifRed._HP <= 0:
        prompting(f"{dresseur1._NOM} a perdu !")
