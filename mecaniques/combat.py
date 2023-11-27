from classes.Pokemon import Pokemon
from classes.Dresseur import Dresseur
from classes.Equipe import Equipe
from classes.Entite import Entite
from functions.prompting import prompting
from functions.prompting import clear_screen
import time

def combat(dresseur1 : Dresseur, dresseur2 : Dresseur, CynthiaPokemon):

    PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
    PokemonActifCynthia = dresseur2._EKIP.get_equipe()[CynthiaPokemon]


    while PokemonActifCynthia._HP > 0:

        if PokemonActifRed._VIT > PokemonActifCynthia._VIT:
            firstPokemon = PokemonActifRed
            secondPokemon = PokemonActifCynthia
        else:
            firstPokemon = PokemonActifCynthia
            secondPokemon = PokemonActifRed

        action = int(input(f"""
                                    
                           ||{secondPokemon._NOM} : {secondPokemon._HP}/{secondPokemon._MAXHP} HP


        ||{firstPokemon._NOM} : {firstPokemon._HP}/{firstPokemon._MAXHP} HP


\n              Que souhaitez-vous faire ?
                        1. Attaquer | 2. Changer de Pokémon """))

        match action:
            case 1:
                clear_screen()
                prompting(f"{firstPokemon._NOM} attaque {secondPokemon._NOM} ! \n")
                firstPokemon.attack(secondPokemon)
                if PokemonActifRed._HP <= 0:
                    prompting(f"{PokemonActifRed._NOM} est KO !")
                    time.sleep(1)
                    clear_screen()
                    print(dresseur1._EKIP.get_equipe()[0:5])
                    next_pokemon = int(input("""Quel Pokémon souhaitez-vous choisir ?"""))
                    dresseur1._EKIP.changepokemon(next_pokemon)
                    
                time.sleep(1)
                clear_screen()
                prompting(f"{secondPokemon._NOM} "+ f" a {secondPokemon._HP}/{secondPokemon._MAXHP} HP restants ! \n")
                time.sleep(0.5)
                prompting(f"{secondPokemon._NOM} attaque {firstPokemon._NOM} !\n")
                secondPokemon.attack(firstPokemon)
                if PokemonActifRed._HP <= 0:
                    prompting(f"{PokemonActifRed._NOM} est KO !")
                    time.sleep(1)
                    clear_screen()
                    print(dresseur1._EKIP.get_equipe()[0:5])
                    int(input("""Quel Pokémon souhaitez-vous choisir ?"""))
                    next_pokemon = int(input("""Quel Pokémon souhaitez-vous choisir ?"""))
                    dresseur1._EKIP.changepokemon(next_pokemon)
                    
                time.sleep(1)
                clear_screen()
            case 2:
                clear_screen()
                print(dresseur1._EKIP.get_equipe()[1:5])
                choix_pokemon = int(input("""Quel Pokémon souhaitez-vous choisir ?"""))
                if choix_pokemon == 1:
                    clear_screen()
                    dresseur1._EKIP.changepokemon(1)
                    prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} !")
                    PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
                    firstPokemon = PokemonActifRed

                    secondPokemon = dresseur2._EKIP.get_equipe()[0]
                    secondPokemon.attack(firstPokemon)
                elif choix_pokemon == 2:
                    clear_screen()
                    dresseur1._EKIP.changepokemon(2)
                    prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} !")
                    PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
                    firstPokemon = PokemonActifRed

                    secondPokemon = dresseur2._EKIP.get_equipe()[0]
                    secondPokemon.attack(firstPokemon)
                elif choix_pokemon == 3:
                    clear_screen()
                    dresseur1._EKIP.changepokemon(3)
                    prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} !")
                    PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
                    firstPokemon = PokemonActifRed

                    secondPokemon = dresseur2._EKIP.get_equipe()[0]
                    secondPokemon.attack(firstPokemon)
                elif choix_pokemon == 4:
                    clear_screen()
                    dresseur1._EKIP.changepokemon(3)
                    prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} !")
                    PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
                    firstPokemon = PokemonActifRed

                    secondPokemon = dresseur2._EKIP.get_equipe()[0]
                    secondPokemon.attack(firstPokemon)
                elif choix_pokemon == 5:
                    clear_screen()
                    dresseur1._EKIP.changepokemon(3)
                    prompting(f"{dresseur1._NOM} a choisi {dresseur1._EKIP.get_equipe()[0]} !")
                    PokemonActifRed = dresseur1._EKIP.get_equipe()[0]
                    firstPokemon = PokemonActifRed

                    secondPokemon = dresseur2._EKIP.get_equipe()[0]
                    secondPokemon.attack(firstPokemon)
                else:
                    prompting("Veuillez choisir un Pokémon valide !")