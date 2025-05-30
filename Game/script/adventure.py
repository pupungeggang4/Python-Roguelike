import random

class Adventure():
    def __init__(self):
        self.floor = 1
        self.layout = [
            [0, 2, 2, 2, 2, 2, 2, 0],
            [0, 2, 2, 2, 2, 2, 2, 0],
            [1, 2, 2, 2, 2, 2, 2, 1],
            [0, 2, 2, 2, 2, 2, 2, 0],
            [0, 2, 2, 2, 2, 2, 2, 0]
        ]

    def generate_layout(self):
        self.layout = [
            [0, 2, 0, 0, 2, 0, 5, 0],
            [0, 2, 0, 0, 2, 0, 5, 0],
            [1, 2, 0, 0, 2, 0, 5, 6],
            [0, 2, 0, 0, 2, 0, 5, 0],
            [0, 2, 0, 0, 2, 0, 5, 0]
        ]
        for i in range(5):
            self.layout[i][2] = random.randint(3, 4)
            self.layout[i][3] = random.randint(3, 4)
            self.layout[i][5] = random.randint(3, 4)