import sys, pygame
from script.module import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    pygame.display.flip()

def mouse_up(game, pos, button):
    pass