import pygame, sys
from script.module import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_start, 2)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_info, 2)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_erase, 2)
    pygame.display.flip()

def mouse_up(game, pos, button):
    if button == 1:
        if point_inside_rect_UI(pos, UI.Title.button_erase):
            erase_data(game)