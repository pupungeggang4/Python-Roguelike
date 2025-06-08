import copy
from script.module import *

class Player():
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.exp_max = 50
        self.gold = 50
        self.hp = 60
        self.energy = 6
        self.attack = 0
        self.hardness = 0
        self.deck = []

    def set_player(self, ID):
        data = copy.deepcopy(Data.character[ID])
        data_d = copy.deepcopy(Data.character_description[ID])
        self.name = data_d['name']
        self.level = 1
        self.exp = 0
        self.exp_max = 50
        self.gold = 50
        self.hp = data['hp']
        self.energy = data['energy']
        self.attack = data['attack']
        self.hardness = data['hardness']
        self.deck = []

        for i in range(len(data['start_deck'])):
            card = Card()
            card.set_data(data['start_deck'][i])
            self.deck.append(card)

        self.weapon = []
        self.equipment = []
        self.item = []