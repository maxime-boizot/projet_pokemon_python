from Pokemon import Pokemon

class Equipe:
    def __init__(self, pokemons : list):
        self._POKEMONS = pokemons

    def __str__(self):
        return f"Mon équipe est composé de {self._POKEMONS}"
    
    def changepokemon(self, pokemons):
        if pokemons in self._POKEMONS:
            index = self._POKEMONS.index(pokemons)
            self._POKEMONS[0], self._POKEMONS[index] = self._POKEMONS[index], self._POKEMONS[0]
        else:
            print("Ce pokemon n'est pas dans votre équipe")



if __name__ == "__main__":
    Dracofoutre = Pokemon("Dracofoutre", 100, 10, 5, 10)
    Tiplouf = Pokemon("Tiplouf", 100, 10, 5, 10)
    Pikachu = Pokemon("Pikachu", 100, 10, 5, 10)
    monekip = Equipe([Dracofoutre, Tiplouf, Pikachu])
    print(monekip)
        
    pass