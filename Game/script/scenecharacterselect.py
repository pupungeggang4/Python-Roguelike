import sys, pygame
from script.module import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.surface.blit(Font.neodgm_32.render('Select Character', False, Color.black), UI.Character_Select.text_title)
    pygame.draw.rect(game.surface, Color.black, UI.Character_Select.button_back, 2)

    for i in range(9):
        pygame.draw.rect(game.surface, Color.black, UI.Character_Select.button_character[i], 2)
        if game.save['unlocked'][i + 1] == False:
            game.surface.blit(Image.locked, UI.Character_Select.button_character[i])
        else:
            game.surface.blit(Image.character[i + 1], UI.Character_Select.button_character[i])

    if game.selected_character != -1:
        game.surface.blit(Image.select_frame, UI.Character_Select.button_character[game.selected_character])

    pygame.draw.rect(game.surface, Color.black, UI.Character_Select.box_description, 2)
    pygame.draw.rect(game.surface, Color.black, UI.Character_Select.button_start, 2)
    game.surface.blit(Font.neodgm_32.render('Start', False, Color.black), UI.Character_Select.text_start)

    pygame.display.flip()

def mouse_up(game, pos, button):
    if button == 1:
        if point_inside_rect_UI(pos, UI.Character_Select.button_back):
            game.scene = 'title'
            game.state = ''

        for i in range(9):
            if point_inside_rect_UI(pos, UI.Character_Select.button_character[i]):
                if game.save['unlocked'][i + 1] == True:
                    game.selected_character = i

        if point_inside_rect_UI(pos, UI.Character_Select.button_start):
            if game.selected_character != -1:
                game.scene = 'map'
                game.state = ''
                game.player.set_player(game.selected_character + 1)
                game.adventure.floor = 1
                game.adventure.generate_layout()