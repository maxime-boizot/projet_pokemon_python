from classes.Pokemon import Pokemon
from classes.Dresseur import Dresseur
from classes.Equipe import Equipe
from classes.Entite import Entite
from functions.prompting import prompting
from functions.prompting import clear_screen
import time

def combat(dresseur1 : Dresseur, dresseur2 : Dresseur, cynthiapokemon):

    PokemonActifCynthia = dresseur2._EKIP.get_equipe()[0]

    def isPokemonDead():
        if dresseur1._EKIP.get_equipe()[0]._HP <= 0:
            prompting(f"{dresseur1._EKIP.get_equipe()[0]._NOM} est KO !")
            time.sleep(1)
            clear_screen()
            print(dresseur1._EKIP.get_equipe()[0:5])
            next_pokemon = int(input("""Quel Pokémon souhaitez-vous choisir ?"""))
            dresseur1._EKIP.changepokemon(next_pokemon)
            prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} !")
        elif dresseur2._EKIP.get_equipe()[0]._HP <= 0:
            prompting(f"{dresseur2._EKIP.get_equipe()[0]._NOM} est KO !")
            time.sleep(1)
            clear_screen()
            if dresseur2._EKIP.lastStandMan():
                dresseur2._EKIP.changepokemon(cynthiapokemon + 1)
                prompting(f"{dresseur2._NOM} a choisi {dresseur2._EKIP.get_equipe()[0]} !")
            else:
                pass

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
            firstPokemon = PokemonActifRed

            secondPokemon = PokemonActifCynthia
            secondPokemon.attack(firstPokemon)
            isPokemonDead()
        else:
            prompting("Ce pokemon ne peux pas se battre !")


    while dresseur2._EKIP.lastStandMan():

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
                case 2:
                    SwapTeamMember()