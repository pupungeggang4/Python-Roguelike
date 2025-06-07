import json

class Card():
    def __init__(self):
        self.ID = 0
        self.name = ''
        self.element = ''
        self.rarity = ''
        self.type = ''
        self.energy = 0
        self.effect = []

    def set_data(self, ID):
        data = json.loads(json.dumps(Data.card[ID]))
        self.ID = ID
        self.name = data['name']