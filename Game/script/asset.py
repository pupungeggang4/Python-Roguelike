import pygame

class Color():
    black = [0, 0, 0]
    white = [255, 255, 255]
    transparent = [0, 0, 0, 0]

class Font():
    neodgm_16 = None
    neodgm_32 = None

class Image():
    icon = {
        'start': None, 'battle': None, 'event': None, 'shop': None, 'rest': None, 'boss': None,
        'card': None, 'equipment': None, 'weapon': None, 'item': None, 'profile': None
    }

    class Button():
        back = None
        menu = None
        info = None
        prev = None
        next = None
        close = None

    locked = None
    select_frame = None
    select_frame_80 = None
    character = {}

    card = {}
    weapon = {}
    equipment = {}
    item = {}

def load_image():
    Image.icon['start'] = pygame.image.load('image/icon/IconStart.png')
    Image.icon['battle'] = pygame.image.load('image/icon/IconBattle.png')
    Image.icon['event'] = pygame.image.load('image/icon/IconEvent.png')
    Image.icon['shop'] = pygame.image.load('image/icon/IconShop.png')
    Image.icon['rest'] = pygame.image.load('image/icon/IconRest.png')
    Image.icon['boss'] = pygame.image.load('image/icon/IconBoss.png')
    Image.icon['card'] = pygame.image.load('image/icon/IconCard.png')
    Image.icon['weapon'] = pygame.image.load('image/icon/IconWeapon.png')
    Image.icon['equipment'] = pygame.image.load('image/icon/IconEquipment.png')
    Image.icon['item'] = pygame.image.load('image/icon/IconItem.png')
    Image.icon['profile'] = pygame.image.load('image/icon/IconProfile.png')

    Image.Button.back = pygame.image.load('image/button/ButtonBack.png')
    Image.Button.menu = pygame.image.load('image/button/ButtonMenu.png')
    Image.Button.info = pygame.image.load('image/button/ButtonInfo.png')
    Image.Button.prev = pygame.image.load('image/button/ButtonPrev.png')
    Image.Button.next = pygame.image.load('image/button/ButtonNext.png')
    Image.Button.close = pygame.image.load('image/button/ButtonClose.png')

    Image.locked = pygame.image.load('image/Locked.png')
    Image.select_frame = pygame.image.load('image/SelectFrame.png')
    Image.select_frame_80 = pygame.image.load('image/SelectFrame80.png')

    Image.character[1] = pygame.image.load('image/Character1.png')

    for i in range(1, 3):
        Image.card[i] = pygame.image.load(f'image//card/Card{str(i).zfill(3)}.png')

    for i in range(1, 2):
        Image.weapon[i] = pygame.image.load(f'image/weapon/Weapon{str(i).zfill(3)}.png')

    for i in range(101, 102):
        Image.equipment[i] = pygame.image.load(f'image/equipment/Equipment{str(i).zfill(3)}.png')

    for i in range(1, 2):
        Image.item[i] = pygame.image.load(f'image/item/Item{str(i).zfill(3)}.png')