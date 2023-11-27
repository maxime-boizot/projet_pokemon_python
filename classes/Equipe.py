from classes.Pokemon import Pokemon

class Equipe:
    def __init__(self, pokemons : list):
        self._POKEMONS = pokemons

    def __str__(self):
        pokemon_names = [str(pokemon) for pokemon in self._POKEMONS]
        return f"Mon équipe est composée de : \n{' '.join(pokemon_names)}"
    
    def get_equipe(self):
        return self._POKEMONS
    
    def changepokemon(self, pokemons):
        if pokemons in self._POKEMONS:
            index = self._POKEMONS.index(pokemons)
            self._POKEMONS[0], self._POKEMONS[index] = self._POKEMONS[index], self._POKEMONS[0]
        else:
            print("Ce pokemon n'est pas dans votre équipe")



if __name__ == "__main__":
    Dracofoutre = Pokemon("Dracofoutre", 100, 20, 2, 5)
    Tiplouf = Pokemon("Tiplouf", 50, 8, 8, 20)
    Pikachu = Pokemon("Pikachu", 35, 12, 10, 25)
    monekip = Equipe([Dracofoutre, Tiplouf, Pikachu])
    print(monekip)

    print('-----------------------------------------')

    monekip.changepokemon(Pikachu)

    print(monekip)
        
    pass