from game_2048.lib.graphics import *


def color(number):
    if number > 4096:
        return color_rgb(0, 0, 0)
    elif number > 2048:
        return color_rgb(50, 50, 50)
    elif number > 1024:
        return color_rgb(250, 150, 0)
    elif number > 512:
        return color_rgb(250, 170, 0)
    elif number > 256:
        return color_rgb(250, 190, 0)
    elif number > 128:
        return color_rgb(250, 210, 0)
    elif number > 64:
        return color_rgb(250, 230, 0)
    elif number > 32:
        return color_rgb(250, 70, 70)
    elif number > 16:
        return color_rgb(250, 90, 90)
    elif number > 8:
        return color_rgb(250, 120, 120)
    elif number > 4:
        return color_rgb(240, 150, 120)
    elif number > 2:
        return color_rgb(240, 230, 140)
    elif number > 1:
        return color_rgb(240, 230, 200)
    else:
        return color_rgb(200, 200, 200)


class Tile:
    def __init__(self, x, y, number, side):
        self.x = x
        self.y = y
        self.number = number
        self.side = side
        self.rect = Rectangle(Point(x - side / 2, y - side / 2), Point(x + side / 2, y + side / 2))
        self.text = Text(Point(x, y), str(number))
        self.rect.setFill(color(number))

    def draw(self, win):
        self.rect.draw(win)
        if self.number == 0:
            self.text.setText("")
        self.text.draw(win)

    def changeNumber(self, number):
        self.number = number
        if self.number!=0:
            self.text.setText(str(number))
        else:
            self.text.setText("")
        self.rect.setFill(color(number))


class Grid:
    def __init__(self, x, y, side):
        self.side = side
        self.x = x
        self.y = y
        self.tiles = [[] for i in range(4)]
        for i in range(4):
            for j in range(4):
                self.tiles[i].append( Tile(x - 1.5 * side/4 + i * side/4, y - 1.5 * side/4 + j * side/4, 0, side / 4))

    def draw(self, win):
        for i in range(4):
            for j in range(4):
                self.tiles[j][i].draw(win)

    def updateTile(self, i, j, number):
        self.tiles[i][j].changeNumber(number)

    def updateGrid(self, arr):
        for i in range(4):
            for j in range(4):
                self.tiles[j][i].changeNumber(arr[i][j])
