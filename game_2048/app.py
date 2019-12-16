from game_2048.lib.graphics import *
from game_2048.data.data_loader import width, height
from game_2048.game import game_round


def run():
    win = GraphWin("2048", width, height)  # create a window
    game_round.round(win,width,height)
