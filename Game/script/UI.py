class UI():
    class Title():
        text_title = [24, 24]
        button_start = [160, 160, 960, 80]
        text_start = [184, 184]
        button_info = [160, 240, 960, 80]
        text_info = [184, 264]
        button_erase = [160, 320, 960, 80]
        text_erase = [184, 344]
        button_exit = [160, 400, 960, 80]
        text_exit = [184, 424]

    class Character_Select():
        text_title = [24, 24]
        button_back = [1180, 20, 80, 80]
        button_character = [
            [40, 120, 160, 160], [240, 120, 160, 160], [440, 120, 160, 160],
            [40, 320, 160, 160], [240, 320, 160, 160], [440, 320, 160, 160],
            [40, 520, 160, 160], [240, 520, 160, 160], [440, 520, 160, 160]
        ]
        box_description = [700, 120, 560, 360]
        text_name = [704, 124]
        text_hp = [704, 324]
        text_energy = [704, 364]
        text_attack = [704, 404]
        text_hardness = [704, 444]
        
        button_start = [1100, 600, 160, 80]
        text_start = [1124, 624]

    class Map():
        text_title = [24, 24]
        button_menu = [1180, 20, 80, 80]
        button_info = [1180, 620, 80, 80]
        element_start = [180, 80]
        element_size = [80, 80]
        element_interval = [120, 120]

        class Info():
            rect = [160, 40, 960, 640]
            button_close = [1080, 40, 40, 40]
            tab_profile = [160, 40, 200, 40]
            icon_profile = [240, 40]
            tab_card = [360, 40, 200, 40]
            icon_card = [440, 40]

            text_name = [164, 84]
            portrait = [200, 120, 160, 160]
            text_level = [164, 364]
            text_exp = [164, 404]
            text_gold = [164, 444]
            text_hp = [164, 484]
            text_energy = [164, 524]
            text_attack = [164, 564]
            text_hardness = [164, 604]
            text_weapon = [404, 84]
            text_equipment = [404, 244]

            equipment = [
                [400, 280, 80, 80], [480, 280, 80, 80], [560, 280, 80, 80], [640, 280, 80, 80], [720, 280, 80, 80],
                [800, 280, 80, 80], [880, 280, 80, 80], [960, 280, 80, 80]
            ]

            text_item = [404, 404]
            item = [[400, 440, 80, 80], [480, 440, 80, 80], [560, 440, 80, 80], [640, 440, 80, 80]]

    class Battle():
        button_menu = [1180, 20, 80, 80]

    class Info():
        text_title = [24, 24]
        button_back = [1180, 20, 80, 80]
        tab_card = [140, 120, 200, 40]
        icon_card = [220, 120]
        tab_weapon = [340, 120, 200, 40]
        icon_weapon = [420, 120]
        tab_equipment = [540, 120, 200, 40]
        icon_equipment = [620, 120]
        tab_item = [740, 120, 200, 40]
        icon_item = [820, 120]

    class Menu():
        rect = [320, 240, 640, 240]
        text_paused = [344, 264]
        button_resume = [320, 320, 640, 80]
        text_resume = [344, 344]
        button_exit = [320, 400, 640, 80]
        text_exit = [344, 424]

    class Card():
        rect = [0, 0, 200, 240]
        energy_rect = [0, 0, 40, 40]
        energy_text = [4, 4]
        image = [20, 20, 160, 120]
        d_text_start = [4, 164]
        d_text_interval = [0, 20]