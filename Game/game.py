import pygame, sys
from script.module import *
import script.scenetitle as scenetitle
import script.scenecharacterselect as scenecharacterselect
import script.scenemap as scenemap
import script.scenebattle as scenebattle
import script.sceneinfo as sceneinfo

class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.load_font()
        load_image()
        self.load_data()

        self.scene = 'title'
        self.state = ''
        self.state_click = ''
        self.menu = False
        self.player_info_tab = ''
        self.player_card_page = 0
        self.info_tab = ''

        self.selected_character = -1

        self.adventure = Adventure()
        self.player = Player()

        self.FPS = 60
        self.save = {}
        load_save_data(self)
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode([1280, 720], pygame.SCALED, vsync = 1)

    def load_font(self):
        Font.neodgm_16 = pygame.font.Font('font/neodgm.ttf', 16)
        Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)

    def load_data(self):
        f = open('data/card.json', 'r')
        d = json.loads(f.read())
        for k in d:
            Data.card[int(k)] = d[k]
        f.close()
        f = open('data/card_description.json', 'r')
        d = json.loads(f.read())
        for k in d:
            Data.card_description[int(k)] = d[k]
        f.close()
        f = open('data/equipment.json', 'r')
        d = json.loads(f.read())
        for k in d:
            Data.equipment[int(k)] = d[k]
        f.close()
        f = open('data/equipment_description.json', 'r')
        d = json.loads(f.read())
        for k in d:
            Data.equipment_description[int(k)] = d[k]
        f.close()
        f = open('data/item.json', 'r')
        d = json.loads(f.read())
        for k in d:
            Data.item[int(k)] = d[k]
        f.close()
        f = open('data/item_description.json', 'r')
        d = json.loads(f.read())
        for k in d:
            Data.item_description[int(k)] = d[k]
        f.close()
        f = open('data/unit.json', 'r')
        d = json.loads(f.read())
        for k in d:
            Data.unit[int(k)] = d[k]
        f.close()
        f = open('data/unit_description.json', 'r')
        d = json.loads(f.read())
        for k in d:
            Data.unit_description[int(k)] = d[k]
        f.close()
        f = open('data/character.json', 'r')
        d = json.loads(f.read())
        for k in d:
            Data.character[int(k)] = d[k]
        f.close()
        f = open('data/character_description.json', 'r')
        d = json.loads(f.read())
        for k in d:
            Data.character_description[int(k)] = d[k]
        f.close()
        f = open('data/weapon.json', 'r')
        d = json.loads(f.read())
        for k in d:
            Data.weapon[int(k)] = d[k]
        f.close()
        f = open('data/weapon_description.json', 'r')
        d = json.loads(f.read())
        for k in d:
            Data.weapon_description[int(k)] = d[k]
        f.close()

    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self.handle_scene()
            self.handle_input()

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)

        elif self.scene == 'character_select':
            scenecharacterselect.loop(self)

        elif self.scene == 'map':
            scenemap.loop(self)

        elif self.scene == 'battle':
            scenebattle.loop(self)

        elif self.scene == 'info':
            sceneinfo.loop(self)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                button = event.button
                
                if self.scene == 'title':
                    scenetitle.mouse_up(self, pos, button)

                elif self.scene == 'character_select':
                    scenecharacterselect.mouse_up(self, pos, button)

                elif self.scene == 'map':
                    scenemap.mouse_up(self, pos, button)

                elif self.scene == 'battle':
                    scenebattle.mouse_up(self, pos, button)

                elif self.scene == 'info':
                    sceneinfo.mouse_up(self, pos, button)

Game().run()