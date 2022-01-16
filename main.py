import pandas as pd
import random as rand
from pokemon import Pokemon

pokedex = pd.read_csv('data/pokedex.csv', 
    usecols = ['pokedex_number', 'name', 'generation',
       'status', 'species', 'type_number', 'type_1', 'type_2', 'height_m',
       'weight_kg', 'abilities_number', 'ability_1', 'ability_2',
       'ability_hidden', 'total_points', 'hp', 'attack', 'defense',
       'sp_attack', 'sp_defense', 'speed', 'catch_rate', 'base_friendship',
       'base_experience', 'growth_rate', 'against_normal',
       'against_fire', 'against_water', 'against_electric', 'against_grass',
       'against_ice', 'against_fight', 'against_poison', 'against_ground',
       'against_flying', 'against_psychic', 'against_bug', 'against_rock',
       'against_ghost', 'against_dragon', 'against_dark', 'against_steel',
       'against_fairy'])
# print(df.info())
# print(pokedex)

images = pd.read_csv('data/pokemon_images.csv',index_col = 0)
# print(images)

pokedex = pokedex.merge(images, left_on = 'pokedex_number', right_on = 'number')
# print(pokedex.columns)


class Pykemon:
    def __init__(self):
        self.get_pokemon()
        pass

    def get_damage(attacking_pokemon, defending_pokemon, move, weather):
        level = attacking_pokemon.level
        A = attacking_pokemon.series # need schema to extract attack stat
        D = defending_pokemon.series

        damage = ((2 * level / 5 + 2) * power * A / D / 50 + 2) * targets * weather * badge * critical * random * STAB * type * burn * other

    def get_pokemon(self):
        pokemon_series = None
        while not isinstance(pokemon_series,pd.DataFrame):
            pokemon_pick = input('Enter a pokemon name/number ')
            try:
                pokemon_pick = int(pokemon_pick)
            except ValueError:
                if pokemon_pick in list(pokedex['name']):
                    pokemon_series = pokedex[pokedex['name'] == pokemon_pick]
                else:
                    print('Please pick a valid pokemon name.')
            else:
                if pokemon_pick in list(pokedex['pokedex_number']):
                    pokemon_series = pokedex[pokedex['pokedex_number'] == pokemon_pick]
                else:
                    print('Please pick a valid pokemon number.')
               

p = Pykemon()

