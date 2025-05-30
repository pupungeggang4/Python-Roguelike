import sys, pygame
from script.module import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    pygame.draw.rect(game.surface, Color.black, UI.Map.button_back, 2)
    pygame.draw.rect(game.surface, Color.black, UI.Map.button_info, 2)
    game.surface.blit(Font.neodgm_32.render('Select', False, Color.black), UI.Map.text_title)

    for i in range(5):
        for j in range(8):
            if game.adventure.layout[i][j] > 0:
                rect = [UI.Map.element_start[0] + UI.Map.element_interval[0] * j, UI.Map.element_start[1] + UI.Map.element_interval[1] * i, UI.Map.element_size[0], UI.Map.element_size[1]]
                img_list = ['', 'start', 'battle', 'event', 'shop', 'rest', 'boss']
                game.surface.blit(Image.icon[img_list[game.adventure.layout[i][j]]], rect)

    pygame.display.flip()

def mouse_up(game, pos, button):
    if button == 1:
        if point_inside_rect_UI(pos, UI.Info.button_back):
            game.scene = 'title'
            game.state = ''