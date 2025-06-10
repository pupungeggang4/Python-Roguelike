import json
from script.module import *

class Weapon():
    def __init__(self):
        self.ID = 0
        self.name = ''
        self.element = ''
        self.rarity = ''
        self.energy = 0
        self.effect = []
        self.description = []

    def set_data(self, ID):
        data = json.loads(json.dumps(Data.weapon[ID]))
        data_d = json.loads(json.dumps(Data.weapon_description[ID]))
        self.ID = ID
        self.name = data['name']
        self.element = data['element']
        self.ratiry = data['rarity']
        self.energy = data['energy']
        self.effect = data['effect']
        self.description = data_d['description']