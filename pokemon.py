import random as rand

class pokemon: 
    def __init__(self, series):
        self.series = series

        self.max_hp = None
        self.current_hp = self.max_hp

        self.moves_learned = None

        self.level = None

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

        self.sprite = series.loc['image_url']
        
    def __repr__(self):
        return self.sprite
    
    def make_move(self):
        pass