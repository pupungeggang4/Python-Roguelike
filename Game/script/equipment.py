import json
from script.module import *

class Equipment():
    def __init__(self):
        self.ID = 0
        self.name = ''
        self.element = ''
        self.rarity = ''
        self.effect = []
        self.description = []

    def set_data(self, ID):
        data = json.loads(json.dumps(Data.equipment[ID]))
        data_d = json.loads(json.dumps(Data.equipment_description[ID]))
        self.ID = ID
        self.name = data['name']
        self.element = data['element']
        self.rarity = data['rarity']
        self.effect = data['effect']
        self.description = data_d['description']