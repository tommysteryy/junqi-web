from enum import Enum

class Cards(Enum):
    juqi = -1
    gobi = 1
    pazh = 2
    lizh = 3
    yizh = 4
    tuzh = 5
    lvzh = 6
    shzh = 7
    juzh = 8
    sili = 9
    zhda = 10
    dile = 11

class Game(Enum):
    OVER = True
    CONTINUE = False


class Player(Enum):
    SELF_DESTRUCT = 0
    RED = 1
    BLACK = 2
    IMPOSSIBLE = 3

validCards = [e.name for e in Cards]