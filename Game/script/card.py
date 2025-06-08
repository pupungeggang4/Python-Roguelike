import pygame, sys, json
from script.module import *

class Card():
    def __init__(self):
        self.ID = 0
        self.name = ''
        self.element = ''
        self.rarity = ''
        self.type = ''
        self.energy = 0
        self.effect = []
        self.description = ''
        self.surface = pygame.surface.Surface([200, 240])

    def set_data(self, ID):
        data = json.loads(json.dumps(Data.card[ID]))
        data_d = json.loads(json.dumps(Data.card_description[ID]))
        self.ID = ID
        self.name = data['name']
        self.element = data['element']
        self.rarity = data['rarity']
        self.type = data['type']
        self.energy = data['energy']
        self.effect = data['effect']
        self.description = data_d['description']

    def render(self, sur, pos):
        self.surface.fill(Color.white)
        pygame.draw.rect(self.surface, Color.black, UI.Card.rect, 2)
        pygame.draw.rect(self.surface, Color.black, UI.Card.image, 2)
        self.surface.blit(Font.neodgm_32.render(f'{self.energy}', False, Color.black), UI.Card.text_energy)
        self.surface.blit(Font.neodgm_16.render(f'{self.name}', False, Color.black), UI.Card.text_name)
        for i in range(len(self.description)):
            d_pos = [UI.Card.text_d_start[0], UI.Card.text_d_start[1] + UI.Card.text_d_interval[1] * i]
            self.surface.blit(Font.neodgm_16.render(self.description[i], False, Color.black), d_pos)
            
        sur.blit(self.surface, pos)

    def clone(self):
        pass