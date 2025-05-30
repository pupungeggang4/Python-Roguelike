import json

empty = {
    'card': [],
    'equipment': [],
    'item': [],
    'unlock': [False, True, False, False, False, False, False, False, False, False]
}

def load_save_data(game):
    try:
        f = open('save/save.txt', 'r')
        game.save = json.loads(f.readline())
        f.close()
    except:
        f = open('save/save.txt', 'w')
        f.write(json.dumps(empty))
        f.close()
        f = open('save/save.txt', 'r')
        game.save = json.loads(f.readline())
        f.close()

def save_data(game):
    f = open('save/save.txt', 'w')
    f.write(json.dumps(game.save))
    f.close()

def erase_data(game):
    f = open('save/save.txt', 'w')
    f.write(json.dumps(empty))
    f.close()
    f = open('save/save.txt', 'r')
    game.save = json.loads(f.readline())
    f.close()