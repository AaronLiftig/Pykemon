import random as rand
import requests

class Pokemon: 
    def __init__(self, series, level = 50, moves = None, item = None):
        self.series = series

        self.level = level

        self.max_hp = None
        self.current_hp = self.max_hp

        self.moves_learned = None

        self.attack = None
        self.defense = None
        self.special_attack = None
        self.special_defense = None

        self.speed = None

        self.nature = None
        self.ability = None

        self.item = None

        self.exp_points = None
        self.exp_to_next_level = None

        self.evasion = None
        self.accuracy = None

    def __repr__(self):
        pass

    def make_move(self):
        pass