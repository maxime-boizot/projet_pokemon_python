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
        firstPokemon = PokemonActifRed
        secondPokemon = PokemonActifCynthia
    else:
        firstPokemon = PokemonActifCynthia
        secondPokemon = PokemonActifRed

    while firstPokemon._HP > 0 or secondPokemon._HP > 0:

        action = int(input("""Que souhaitez-vous faire ?
                        1. Attaquer | 2. Changer de Pokémon """))

        match action:
            case 1:
                prompting(f"{firstPokemon} attaque {secondPokemon} !")
                firstPokemon.attack(secondPokemon)
                time.sleep(1)
                clear_screen()
                prompting(f"{secondPokemon} a {secondPokemon._HP} HP restants !")
                prompting(f"{secondPokemon} attaque {firstPokemon} !")
                secondPokemon.attack(firstPokemon)
                prompting(f"{firstPokemon} a {firstPokemon._HP} HP restants !")
                clear_screen()
            case 2:
                choix_pokemon = int(input("""Quel Pokémon souhaitez-vous choisir ?
                                    1. Pokemon 1 | 2. Pokemon 2 | 3. Pokemon """))
                if choix_pokemon == 1:
                    dresseur1._EKIP.changepokemon(1)
                    prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} !")
                    PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
                    firstPokemon = PokemonActifRed

                    secondPokemon = dresseur2._EKIP.get_equipe()[0]
                    secondPokemon.attack(firstPokemon)
                elif choix_pokemon == 2:
                    dresseur1._EKIP.changepokemon(2)
                    prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} !")
                    PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
                    firstPokemon = PokemonActifRed

                    secondPokemon = dresseur2._EKIP.get_equipe()[0]
                    secondPokemon.attack(firstPokemon)
                elif choix_pokemon == 3:
                    dresseur1._EKIP.changepokemon(3)
                    prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} !")
                    PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
                    firstPokemon = PokemonActifRed

                    secondPokemon = dresseur2._EKIP.get_equipe()[0]
                    secondPokemon.attack(firstPokemon)
                elif choix_pokemon == 4:
                    dresseur1._EKIP.changepokemon(3)
                    prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} !")
                    PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
                    firstPokemon = PokemonActifRed

                    secondPokemon = dresseur2._EKIP.get_equipe()[0]
                    secondPokemon.attack(firstPokemon)
                elif choix_pokemon == 5:
                    dresseur1._EKIP.changepokemon(3)
                    prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} !")
                    PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
                    firstPokemon = PokemonActifRed

                    secondPokemon = dresseur2._EKIP.get_equipe()[0]
                    secondPokemon.attack(firstPokemon)
                else:
                    prompting("Veuillez choisir un Pokémon valide !")

