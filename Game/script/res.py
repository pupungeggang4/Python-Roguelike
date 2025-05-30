import pygame

class Color():
    black = [0, 0, 0]
    white = [255, 255, 255]

class Font():
    neodgm_32 = None

class Image():
    icon = {
        'start': None, 'battle': None, 'event': None, 'shop': None, 'rest': None, 'boss': None
    }
    locked = None
    select_frame = None
    character = [0, None]

def load_image():
    Image.icon['start'] = pygame.image.load('image/IconStart.png')
    Image.icon['battle'] = pygame.image.load('image/IconBattle.png')
    Image.icon['event'] = pygame.image.load('image/IconEvent.png')
    Image.icon['shop'] = pygame.image.load('image/IconShop.png')
    Image.icon['rest'] = pygame.image.load('image/IconRest.png')
    Image.icon['boss'] = pygame.image.load('image/IconBoss.png')
    Image.locked = pygame.image.load('image/Locked.png')
    Image.select_frame = pygame.image.load('image/SelectFrame.png')

    Image.character[1] = pygame.image.load('image/Character1.png')