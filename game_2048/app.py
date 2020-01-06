from game_2048.lib.graphics import GraphWin, color_rgb
from game_2048.data.settings_loader import window_width, window_height
from game_2048.game import game_round


def run():
    win = GraphWin("2048", window_width, window_height, autoflush=False)  # creating a window
    win.setBackground(color_rgb(245, 245, 195))  # setting background color
    game_round.round(win, window_width, window_height)  # starting the game
