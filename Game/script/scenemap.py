import sys, pygame
from script.module import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.surface.blit(Image.Button.menu, UI.Map.button_menu)
    game.surface.blit(Image.Button.info, UI.Map.button_info)
    game.surface.blit(Font.neodgm_32.render('Select', False, Color.black), UI.Map.text_title)

    for i in range(5):
        for j in range(8):
            if game.adventure.layout[i][j] > 0:
                rect = [UI.Map.element_start[0] + UI.Map.element_interval[0] * j, UI.Map.element_start[1] + UI.Map.element_interval[1] * i, UI.Map.element_size[0], UI.Map.element_size[1]]
                img_list = ['', 'start', 'battle', 'event', 'shop', 'rest', 'boss']
                game.surface.blit(Image.icon[img_list[game.adventure.layout[i][j]]], rect)

    if game.state == 'info':
        Render.render_info(game.surface, game.player)

    if game.menu == True:
        Render.render_menu(game.surface)

    pygame.display.flip()

def mouse_up(game, pos, button):
    if button == 1:
        if game.menu == False:
            if point_inside_rect_UI(pos, UI.Map.button_menu):
                game.menu = True

            if game.state == '':
                if point_inside_rect_UI(pos, UI.Map.button_info):
                    game.state = 'info'
                    game.player_info_tab = 'profile'

            elif game.state == 'info':
                if point_inside_rect_UI(pos, UI.Map.button_info):
                    game.state = ''

        if game.menu == True:
            if point_inside_rect_UI(pos, UI.Menu.button_resume):
                game.menu = False
            elif point_inside_rect_UI(pos, UI.Menu.button_exit):
                game.menu = False
                game.scene = 'title'
                game.state = ''