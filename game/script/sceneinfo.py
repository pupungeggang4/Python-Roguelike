import sys, pygame
from script.module import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.surface.blit(Image.Button.back, UI.Info.button_back)
    game.surface.blit(Font.neodgm_32.render('You Found...', False, Color.black), UI.Info.text_title)
    pygame.draw.rect(game.surface, Color.black, UI.Info.tab_card, 2)
    game.surface.blit(Image.icon['card'], UI.Info.icon_card)
    pygame.draw.rect(game.surface, Color.black, UI.Info.tab_weapon, 2)
    game.surface.blit(Image.icon['weapon'], UI.Info.icon_weapon)
    pygame.draw.rect(game.surface, Color.black, UI.Info.tab_equipment, 2)
    game.surface.blit(Image.icon['equipment'], UI.Info.icon_equipment)
    pygame.draw.rect(game.surface, Color.black, UI.Info.tab_item, 2)
    game.surface.blit(Image.icon['item'], UI.Info.icon_item)
    pygame.display.flip()

def mouse_up(game, pos, button):
    if button == 1:
        if point_inside_rect_UI(pos, UI.Info.button_back):
            game.scene = 'title'
            game.state = ''