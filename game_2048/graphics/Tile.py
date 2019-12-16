from game_2048.lib.graphics import *


class Tile:
    def __init__(self, x, y, number, side):
        self.x = x
        self.y = y
        self.number = number
        self.side = side
        self.rect = Rectangle(Point(x - side / 2, y - side / 2), Point(x + side / 2, y + side / 2))
        self.text = Text(Point(x, y), str(number))

    def draw(self, win):
        self.rect.draw(win)
        self.text.draw(win)

    def move(self, dir, step):
        if dir == 1:
            self.y -= self.side * step
        elif dir == 2:
            self.x += self.side * step
        elif dir == 3:
            self.y += self.side * step
        elif dir == 4:
            self.x -= self.side * step
