import json

empty = {
    1: [1, 2, 3]
}

def load_data(game):
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