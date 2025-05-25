import sys, pygame
from script.module import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    pygame.draw.rect(game.surface, Color.black, UI.Map.button_back, 2)
    game.surface.blit(Font.neodgm_32.render('Select', False, Color.black), UI.Map.text_title)
    pygame.display.flip()

def mouse_up(game, pos, button):
    if button == 1:
        if point_inside_rect_UI(pos, UI.Info.button_back):
            game.scene = 'title'
            game.state = ''