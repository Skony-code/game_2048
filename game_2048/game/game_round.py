from random import randint
from copy import deepcopy
from game_2048.game.game_controls import arrow_key
from game_2048.gui.tiles import *
from game_2048.data import settings_loader


class Board:
    # represents 2048 board's logic
    def __init__(self, win):
        self.win= win
        self.board = [[0] * 4 for i in range(4)]
        self.grid = Grid(settings_loader.window_width / 2, settings_loader.window_height / 2, settings_loader.grid_side,
                         win)
        self.grid.draw()
        self.add_random_tile()
        self.scor = Score(settings_loader.window_width / 2 + settings_loader.grid_side / 2 + 120, 40, win,int(settings_loader.grid_side/18))# creates score graphic object

    def if_end(self):
        # checks if the game should end
        # returns False if there are any 0 in board or if there is no identical numbers next to each other
        # otherwise returns True
        for i in range(len(self.board) - 1):
            for j in range(len(self.board) - 1):
                if self.board[i][j] == self.board[i + 1][j] or self.board[i][j] == self.board[i][j + 1]:
                    return False
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    return False
        for i in range(len(self.board) - 1):
            if self.board[3][i] == self.board[3][i + 1] or self.board[i][3] == self.board[i + 1][3]:
                return False
        return True

    def end(self):
        # displays game over and freezes the game
        text = Text(Point(settings_loader.window_width / 2, settings_loader.window_height / 2), "GAME OVER")
        text.setSize(36)
        text.draw(self.win)
        update()
        text.undraw()

    def add_random_tile(self):
        # adds random 2 or 4 to the board as well as starts spawn animation
        # counts how many 0 are in board and takes random number(x) from 0 to how many 0 there are in the board
        # then it goes through the board until it finds x zeroes, and puts either 2 or 4 in its place
        x = sum(row.count(0) for row in self.board)
        y = randint(0, x - 1)
        z = -1
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    z += 1
                    if z == y:
                        if randint(0, 2) != 1:
                            self.board[i][j] = 2
                            self.grid.animate_spawn(i, j, settings_loader.spawning_time, 2)
                        else:
                            self.board[i][j] = 4
                            self.grid.animate_spawn(i, j, settings_loader.spawning_time, 4)
        self.grid.update(self.board)

    def move(self, direction):
        # changes numbers in the board as well as starts appropriate animations
        if_doub = [[False] * 4 for i in range(4)] # will hold info if the tile has already doubled in current move
        # this is in order to prevent each tile form doubling more than one time
        for h in range(3):
            animation_slide = [[False] * 4 for i in range(4)]  # creates bool list for sliding tiles for animation
            animation_double = [[False] * 4 for i in range(4)]  # creates bool list for doubling tiles for animation
            if direction == 1:
                for i in range(1, 4):
                    for j in range(4):
                        if self.board[i - 1][j] == 0 and self.board[i][j] != 0:
                            self.board[i - 1][j] = self.board[i][j]
                            self.board[i][j] = 0
                            if_doub[i - 1][j] = if_doub[i][j]
                            if_doub[i][j] = False
                            animation_slide[i][j] = True
                        elif self.board[i - 1][j] == self.board[i][j] and self.board[i][j] != 0 and not if_doub[i - 1][
                            j] and not if_doub[i][j]:
                            self.board[i - 1][j] *= 2
                            self.board[i][j] = 0
                            animation_slide[i][j] = True
                            animation_double[j][i - 1] = True
                            if_doub[i - 1][j] = True
                            if_doub[i][j] = False
            elif direction == 2:
                for i in range(2, -1, -1):
                    for j in range(4):
                        if self.board[j][i + 1] == 0 and self.board[j][i] != 0:
                            self.board[j][i + 1] = self.board[j][i]
                            self.board[j][i] = 0
                            if_doub[j][i + 1] = if_doub[j][i]
                            if_doub[j][i] = False
                            animation_slide[i][j] = True
                        elif self.board[j][i + 1] == self.board[j][i] and self.board[j][i] != 0 and not if_doub[j][
                            i + 1] and not if_doub[j][i]:
                            self.board[j][i + 1] *= 2
                            self.board[j][i] = 0
                            animation_slide[i][j] = True
                            animation_double[i + 1][j] = True
                            if_doub[j][i + 1] = True
                            if_doub[j][i] = False
            elif direction == 3:
                for i in range(2, -1, -1):
                    for j in range(4):
                        if self.board[i + 1][j] == 0 and self.board[i][j] != 0:
                            self.board[i + 1][j] = self.board[i][j]
                            self.board[i][j] = 0
                            if_doub[i + 1][j] = if_doub[i][j]
                            if_doub[i][j] = False
                            animation_slide[i][j] = True
                        elif self.board[i + 1][j] == self.board[i][j] and self.board[i][j] != 0 and not if_doub[i + 1][
                            j] and not if_doub[i][j]:
                            self.board[i + 1][j] *= 2
                            self.board[i][j] = 0
                            animation_slide[i][j] = True
                            animation_double[j][i + 1] = True
                            if_doub[i + 1][j] = True
                            if_doub[i][j] = False
            elif direction == 4:
                for i in range(1, 4):
                    for j in range(4):
                        if self.board[j][i - 1] == 0 and self.board[j][i] != 0:
                            self.board[j][i - 1] = self.board[j][i]
                            self.board[j][i] = 0
                            if_doub[j][i - 1] = if_doub[j][i]
                            if_doub[j][i] = False
                            animation_slide[i][j] = True
                        elif self.board[j][i - 1] == self.board[j][i] and self.board[j][i] != 0 and not if_doub[j][
                            i - 1] and not if_doub[j][i]:
                            self.board[j][i - 1] *= 2
                            self.board[j][i] = 0
                            animation_slide[i][j] = True
                            animation_double[i - 1][j] = True
                            if_doub[j][i - 1] = True
                            if_doub[j][i] = False
            self.grid.animate(self.board, animation_slide, animation_double, direction, settings_loader.sliding_time,
                              settings_loader.doubling_time)
            self.grid.update(self.board)
            self.scor.change(self.get_score())


    def get_score(self):
        x = self.board[0][0]
        for i in range(4):
            for j in range(4):
                if self.board[i][j] > x: x = self.board[i][j]
        return x

    def get(self):
        return self.board

    def print(self):
        print('\n'.join(map(''.join, (str(x) for x in self.board))))

    def restart(self):
        self.board = [[0] * 4 for i in range(4)]
        self.grid.update(self.board)



def round(win):
    board = Board(win)#creates board
    while True:
        board.add_random_tile()#adds tile (2 or 4)
        arr2 = deepcopy(board.get())
        board.print()
        print(board.get_score())
        if board.if_end():
            # displays game over if there is no move possible
            board.end()
            board.restart()
        while arr2 == board.get():
            # checks for key until board arrangement has changed
            board.move(arrow_key())
