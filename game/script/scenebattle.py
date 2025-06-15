import sys, pygame
from script.module import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.surface.blit(Image.Button.menu, UI.Battle.button_menu)
    pygame.display.flip()

def mouse_up(game, pos, button):
    pass