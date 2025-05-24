import pygame, sys
from script.module import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.scene = 'title'
        self.state = ''
        self.state_click = ''
        self.FPS = 60
        save = {}
        load_data(self)
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode([1280, 720], pygame.SCALED, vsync = 1)

    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self.handle_scene()
            self.handle_input()

    def handle_scene(self):
        pass

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

Game().run()