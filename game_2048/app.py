from game_2048.lib.graphics import *
from game_2048.data.data_loader import width,height
def run():
    win = GraphWin("2048",width, height) # create a window
    win.getMouse()