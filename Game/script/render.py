import pygame
from script.module import *

class Render():
    @staticmethod
    def render_menu(surface):
        pygame.draw.rect(surface, Color.white, UI.Menu.rect)
        pygame.draw.rect(surface, Color.black, UI.Menu.rect, 2)
        surface.blit(Font.neodgm_32.render('Paused', False, Color.black), UI.Menu.text_paused)
        pygame.draw.rect(surface, Color.black, UI.Menu.button_resume, 2)
        surface.blit(Font.neodgm_32.render('Resume', False, Color.black), UI.Menu.text_resume)
        pygame.draw.rect(surface, Color.black, UI.Menu.button_exit, 2)
        surface.blit(Font.neodgm_32.render('Exit', False, Color.black), UI.Menu.text_exit)

    def render_info(surface, player):
        pygame.draw.rect(surface, Color.white, UI.Map.Info.rect)
        pygame.draw.rect(surface, Color.black, UI.Map.Info.rect, 2)