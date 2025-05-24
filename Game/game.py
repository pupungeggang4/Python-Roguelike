import pygame, sys
from script.module import *
import script.scenetitle as scenetitle
import script.scenemap as scenemap
import script.scenebattle as scenebattle

class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.load_font()
        self.load_image()
        self.scene = 'title'
        self.state = ''
        self.state_click = ''
        self.FPS = 60
        save = {}
        load_data(self)
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode([1280, 720], pygame.SCALED, vsync = 1)

    def load_font(self):
        Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)

    def load_image(self):
        pass

    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self.handle_scene()
            self.handle_input()

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)

        elif self.scene == 'map':
            scenemap.loop(self)

        elif self.scene == 'battle':
            scenebattle.loop(self)

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

                elif self.scene == 'map':
                    scenemap.mouse_up(self, pos, button)

                elif self.scene == 'battle':
                    scenebattle.mouse_up(self, pos, button)

Game().run()