from classes.Pokemon import Pokemon
from classes.Dresseur import Dresseur
from classes.Equipe import Equipe
from classes.Entite import Entite
from functions.prompting import prompting
from functions.prompting import clear_screen
from functions.dice import doubledice
from lore.cynthiaLines import *
from lore.interactionsLines import *
import time

def lastfight(dresseur1: Dresseur, dresseur2: Dresseur):
    dice_stat = doubledice()
    dresseur2._ATK += dice_stat[0]
    dresseur2._DEF += dice_stat[1]

    def SwapTeamMember():
        clear_screen()
        print(dresseur1._EKIP.get_equipe()[0:5])
        choix_pokemon = int(input("""Quel Pokémon souhaitez-vous choisir ?"""))
        if 1 <= choix_pokemon <= 5:
            clear_screen()
            if dresseur1._EKIP.get_equipe()[choix_pokemon]._HP == 0:
                prompting("Ce pokemon ne peux pas se battre !")
                print(dresseur1._EKIP.get_equipe()[0:5])
                choix_pokemon = int(input("""Quel Pokémon souhaitez-vous choisir ?"""))
            dresseur1._EKIP.changepokemon(choix_pokemon)
            prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} !")
            PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
            firstStrike = PokemonActifRed

            secondStrike = dresseur2
            secondStrike.attack(firstStrike)
            isPokemonDead()
        else:
            prompting("Ce pokemon ne peux pas se battre !")

    def isPokemonDead():
        if dresseur1._EKIP.get_equipe()[0]._HP <= 0:
            prompting(f"{dresseur1._EKIP.get_equipe()[0]._NOM} est KO !")
            time.sleep(1)
            clear_screen()
            print(dresseur1._EKIP.get_equipe()[0:5])
            next_pokemon = int(input("""Quel Pokémon souhaitez-vous choisir ?"""))
            dresseur1._EKIP.changepokemon(next_pokemon)
            prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} !")

    prompting(cynthiaEntersFight)
    time.sleep(1)
    clear_screen()
    prompting(in_fight2)

    while dresseur2._HP > 0:

        action = int(input(f"""
                                        
                            ||{dresseur2._NOM} : {dresseur2._HP}/{dresseur2._MAXHP} HP


            ||{dresseur1._EKIP.get_equipe()[0]._NOM} : {dresseur1._EKIP.get_equipe()[0]._HP}/{dresseur1._EKIP.get_equipe()[0]._MAXHP} HP


    \n              Que souhaitez-vous faire ?
                            1. Attaquer | 2. Changer de Pokémon """))

        match action:
            case 1:
                if dresseur1._EKIP.get_equipe()[0]._VIT > dresseur2._VIT:
                    firstStrike = dresseur1._EKIP.get_equipe()[0]
                    secondStrike = dresseur2
                else:
                    firstStrike = dresseur2
                    secondStrike = dresseur1._EKIP.get_equipe()[0]

                clear_screen()
                prompting(f"{firstStrike._NOM} attaque {secondStrike._NOM} ! \n")
                firstStrike.attack(secondStrike)
                isPokemonDead()
                secondStrike.attack(firstStrike)
                isPokemonDead()
            case 2:
                SwapTeamMember()

    prompting(cynthiaDefeat)
    time.sleep(3)
    clear_screen()

    prompting(afterfight)
    time.sleep(2)
    clear_screen()