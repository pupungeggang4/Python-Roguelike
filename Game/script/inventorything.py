import pygame, json
from script.module import *

class InventoryThing():
    def __init__(self):
        self.ID = 0
        self.name = ''
        self.element = ''
        self.rarity = ''
        self.effect = []
        self.description = []
        self.surface = pygame.surface.Surface([80, 80], pygame.SRCALPHA)

    def set_data(self, data, data_d):
        self.name = data['name']
        self.element = data['element']
        self.rarity = data['rarity']
        self.effect = data['effect']
        self.description = data_d['description']

class Weapon(InventoryThing):
    def __init__(self):
        super().__init__()

    def set_data(self, ID):
        data = json.loads(json.dumps(Data.weapon[ID]))
        data_d = json.loads(json.dumps(Data.weapon_description[ID]))
        self.ID = ID
        super().set_data(data, data_d)
        self.energy = data['energy']

    def render(self, surface, pos):
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.weapon[self.ID])
        surface.blit(self.surface, pos)

class Equipment(InventoryThing):
    def __init__(self):
        super().__init__()

    def set_data(self, ID):
        data = json.loads(json.dumps(Data.equipment[ID]))
        data_d = json.loads(json.dumps(Data.equipment_description[ID]))
        self.ID = ID
        super().set_data(data, data_d)

    def render(self, surface, pos):
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.equipment[self.ID])
        surface.blit(self.surface, pos)

class Item(InventoryThing):
    def __init__(self):
        super().__init__()

    def set_data(self, ID):
        data = json.loads(json.dumps(Data.item[ID]))
        data_d = json.loads(json.dumps(Data.item_description[ID]))
        self.ID = ID
        super().set_data(data, data_d)

    def render(self, surface, pos):
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.item[self.ID])
        surface.blit(self.surface, pos)