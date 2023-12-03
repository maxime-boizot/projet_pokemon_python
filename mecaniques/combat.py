from classes.Pokemon import Pokemon
from classes.Dresseur import Dresseur
from classes.Equipe import Equipe
from classes.Entite import Entite
from functions.prompting import prompting
from lore.cynthiaLines import *
from functions.prompting import clear_screen
from functions.dice import doubledice
from functions.dice import dice
import time



def combat(dresseur1 : Dresseur, dresseur2 : Dresseur, cynthiapokemon):
    compteur = 0    
    PokemonActifCynthia = dresseur2._EKIP.get_equipe()[0]
    default_ATK = dresseur1._EKIP.get_equipe()[0]._ATK

    def isPokemonDead():
        nonlocal PokemonActifCynthia
        nonlocal compteur 
        if dresseur1._EKIP.get_equipe()[0]._HP <= 0:
            prompting(f"{dresseur1._EKIP.get_equipe()[0]._NOM} est KO !")
            time.sleep(1)
            clear_screen()
            print(dresseur1._EKIP.get_equipe()[0:5])
            next_pokemon = int(input("""Quel Pokémon souhaitez-vous choisir ?"""))
            dresseur1._EKIP.changepokemon(next_pokemon)
            prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} ")
        elif dresseur2._EKIP.get_equipe()[0]._HP <= 0:
            prompting(f"{dresseur2._EKIP.get_equipe()[0]._NOM} est KO !")
            time.sleep(1)
            clear_screen()
            if dresseur2._EKIP.lastStandMan():
                dresseur2._EKIP.get_equipe().pop(0)
                dresseur2._EKIP.changepokemon(cynthiapokemon)

                PokemonActifCynthia = dresseur2._EKIP.get_equipe()[0]
                compteur += 1
                match compteur:
                    case 3:
                        prompting("Cynthia :\n")
                        prompting(in_fight1)
                        time.sleep(1)
                        clear_screen()
                    case 4:
                        prompting("Cynthia :\n")
                        prompting(cynthiaLastPkmn)
                        time.sleep(1)
                        clear_screen()
                prompting(f"{dresseur2._NOM} a choisi {dresseur2._EKIP.get_equipe()[0]}")
                time.sleep(1)
                clear_screen()
            else:
                pass

    def SwapTeamMember():
        nonlocal default_ATK 
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
            firstPokemon = PokemonActifRed

            secondPokemon = PokemonActifCynthia
            secondPokemon.attack(firstPokemon)
            isPokemonDead()
        else:
            prompting("Ce pokemon ne peux pas se battre !")


    while dresseur2._EKIP.lastStandMan():
            pokemonActif = dresseur1._EKIP.get_equipe()[0]
            default_ATK = dresseur1._EKIP.get_equipe()[0]._ATK
            dice_stat = dice()
            dresseur1._EKIP.get_equipe()[0]._ATK += dice_stat
            prompting(f"Cynthia lance un dé ! {pokemonActif._NOM} voit son ATK modifiée de {dice_stat} !\n")
            time.sleep(1)
            clear_screen()
            action = int(input(f"""
                                        
                            ||{dresseur2._EKIP.get_equipe()[0]._NOM} : {dresseur2._EKIP.get_equipe()[0]._HP}/{dresseur2._EKIP.get_equipe()[0]._MAXHP} HP


            ||{dresseur1._EKIP.get_equipe()[0]._NOM} : {dresseur1._EKIP.get_equipe()[0]._HP}/{dresseur1._EKIP.get_equipe()[0]._MAXHP} HP


    \n              Que souhaitez-vous faire ?
                            1. Attaquer | 2. Changer de Pokémon """))

            match action:
                case 1:
                    if dresseur1._EKIP.get_equipe()[0]._VIT > dresseur2._EKIP.get_equipe()[0]._VIT:
                        firstPokemon = dresseur1._EKIP.get_equipe()[0]
                        secondPokemon = dresseur2._EKIP.get_equipe()[0]
                    else:
                        firstPokemon = dresseur2._EKIP.get_equipe()[0]
                        secondPokemon = dresseur1._EKIP.get_equipe()[0]
                        
                    clear_screen()
                    prompting(f"{firstPokemon._NOM} attaque {secondPokemon._NOM} ! \n")
                    firstPokemon.attack(secondPokemon)
                    isPokemonDead()
                    time.sleep(0.5)
                    secondPokemon.attack(firstPokemon)
                    isPokemonDead()
                    clear_screen()
                case 2:
                    SwapTeamMember()
                    time.sleep(0.5)
                    clear_screen()
            