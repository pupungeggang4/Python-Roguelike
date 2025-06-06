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

    def render_info(game, surface, player):
        pygame.draw.rect(surface, Color.white, UI.Map.Info.rect)
        pygame.draw.rect(surface, Color.black, UI.Map.Info.rect, 2)
        surface.blit(Image.Button.close, UI.Map.Info.button_close)
        pygame.draw.rect(surface, Color.black, UI.Map.Info.tab_profile, 2)
        surface.blit(Image.icon['profile'], UI.Map.Info.icon_profile)
        pygame.draw.rect(surface, Color.black, UI.Map.Info.tab_card, 2)
        surface.blit(Image.icon['card'], UI.Map.Info.icon_card)

        if game.player_info_tab == 'profile':
            pygame.draw.rect(surface, Color.black, UI.Map.Info.portrait, 2)
            surface.blit(Font.neodgm_32.render(f'{player.name}', False, Color.black), UI.Map.Info.text_name)
            surface.blit(Font.neodgm_32.render(f'Lv.{player.level}', False, Color.black), UI.Map.Info.text_level)
            surface.blit(Font.neodgm_32.render(f'Exp: {player.exp}/{player.exp_max}', False, Color.black), UI.Map.Info.text_exp)
            surface.blit(Font.neodgm_32.render(f'Gold: {player.gold}', False, Color.black), UI.Map.Info.text_gold)
            surface.blit(Font.neodgm_32.render(f'HP: {player.hp}', False, Color.black), UI.Map.Info.text_hp)
            surface.blit(Font.neodgm_32.render(f'Energy: {player.energy}', False, Color.black), UI.Map.Info.text_energy)
            surface.blit(Font.neodgm_32.render(f'Attack: {player.attack}', False, Color.black), UI.Map.Info.text_attack)
            surface.blit(Font.neodgm_32.render(f'Hardness: {player.hardness}', False, Color.black), UI.Map.Info.text_hardness)

            surface.blit(Font.neodgm_32.render(f'Weapon', False, Color.black), UI.Map.Info.text_weapon)
            surface.blit(Font.neodgm_32.render(f'Equipment', False, Color.black), UI.Map.Info.text_equipment)
            for i in range(8):
                pygame.draw.rect(surface, Color.black, UI.Map.Info.equipment[i], 2)
            surface.blit(Font.neodgm_32.render(f'Item', False, Color.black), UI.Map.Info.text_item)
            for i in range(4):
                pygame.draw.rect(surface, Color.black, UI.Map.Info.item[i], 2)
        elif game.player_info_tab == 'card':
            pass