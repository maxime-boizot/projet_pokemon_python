from classes.Pokemon import Pokemon
from classes.Dresseur import Dresseur
from classes.Equipe import Equipe
from classes.Entite import Entite
from functions.prompting import prompting
from functions.prompting import clear_screen
import time


def combat(dresseur1 : Dresseur, dresseur2 : Dresseur):

    PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
    PokemonActifCynthia = dresseur2._EKIP.get_equipe()[0]

    if PokemonActifRed._VIT > PokemonActifCynthia._VIT:
        firstStrike = PokemonActifRed
        secondStrike = PokemonActifCynthia
    else:
        firstStrike = PokemonActifCynthia
        secondStrike = PokemonActifRed

    while firstStrike._HP > 0 or secondStrike._HP > 0:

        action = int(input("""Que souhaitez-vous faire ?
                        1. Attaquer | 2. Changer de Pokémon """))

        match action:
            case 1:
                prompting(f"{firstStrike} attaque {secondStrike} !")
                firstStrike.attack(secondStrike)
                time.sleep(1)
                clear_screen()
                prompting(f"{secondStrike} a {secondStrike._HP} HP restants !")
                prompting(f"{secondStrike} attaque {firstStrike} !")
                secondStrike.attack(firstStrike)
                prompting(f"{firstStrike} a {firstStrike._HP} HP restants !")
                clear_screen()
            case 2:
                choix_pokemon = int(input("""Quel Pokémon souhaitez-vous choisir ?
                                    1. Pokemon 1 | 2. Pokemon 2 | 3. Pokemon """))
                if choix_pokemon == 1:
                    dresseur1._EKIP.changepokemon(1)
                elif choix_pokemon == 2:
                    dresseur1._EKIP.changepokemon(2)
                elif choix_pokemon == 3:
                    dresseur1._EKIP.changepokemon(3)
                else:
                    prompting("Veuillez choisir un Pokémon valide !")
    #     prompting(f"{PokemonActifCynthia} attaque {dresseur1._NOM} !")
    #     PokemonActifRed._HP -= dresseur2.Equipe._MEMBRES[0]._ATK
    #     prompting(f"{dresseur1._NOM} a {PokemonActifRed._HP} HP restants !")
    # if PokemonActifCynthia <= 0:
    #     prompting(f"{PokemonActifCynthia} a perdu !")
    # elif PokemonActifRed._HP <= 0:
    #     prompting(f"{dresseur1._NOM} a perdu !")

