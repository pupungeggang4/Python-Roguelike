import pygame, sys
from script.module import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.surface.blit(Font.neodgm_32.render('Roguelike', False, Color.black), UI.Title.text_title)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_start, 2)
    game.surface.blit(Font.neodgm_32.render('Start Game', False, Color.black), UI.Title.text_start)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_info, 2)
    game.surface.blit(Font.neodgm_32.render('Info', False, Color.black), UI.Title.text_info)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_erase, 2)
    game.surface.blit(Font.neodgm_32.render('Erase Data', False, Color.black), UI.Title.text_erase)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_exit, 2)
    game.surface.blit(Font.neodgm_32.render('Exit', False, Color.black), UI.Title.text_exit)
    pygame.display.flip()

def mouse_up(game, pos, button):
    if button == 1:
        if point_inside_rect_UI(pos, UI.Title.button_start):
            game.scene = 'character_select'
            game.state = ''
            game.selected_character = -1

        if point_inside_rect_UI(pos, UI.Title.button_info):
            game.scene = 'info'
            game.state = ''
            game.info_tab = 'card'

        if point_inside_rect_UI(pos, UI.Title.button_erase):
            erase_data(game)

        if point_inside_rect_UI(pos, UI.Title.button_exit):
            pygame.quit()
            sys.exit()