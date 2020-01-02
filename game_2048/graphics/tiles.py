from game_2048.lib.graphics import *
import time


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
    def __init__(self, x, y, number, side, win):
        self.x = x
        self.y = y
        self.number = number
        self.side = side
        self.win = win
        self.rect = Rectangle(Point(x - side / 2, y - side / 2), Point(x + side / 2, y + side / 2))
        self.text = Text(Point(x, y), str(number))
        self.text.setSize(int(side / 5))
        self.rect.setFill(color(number))

    def draw(self):
        self.rect.draw(self.win)
        if self.number == 0:
            self.text.setText("")
        self.text.draw(self.win)

    def changeNumber(self, number):
        self.number = number
        if self.number != 0:
            self.text.setText(str(number))
        else:
            self.text.setText("")
        self.rect.setFill(color(number))

    def move(self, x, y):
        self.rect.move(x, y)
        self.text.move(x, y)

    def undraw(self):
        self.rect.undraw()
        self.text.undraw()

    def doubleanimation(self, tim):
        ar = []
        for i in range(int(tim / 2 * 30)):
            ar.append(Tile(self.x, self.y, self.number, self.side + i / tim * 2, self.win))
            ar[i].draw()
            update(30)
        for i in range(int(tim / 2 * 30) - 1, -1, -1):
            ar[i].undraw()
            update(30)
        del ar

    def moveanimation(self, tiles, dir, tim, win):
        tile = self.rect.clone()
        tiletext = self.text.clone()
        tiletext.setText(str(self.number))
        self.changeNumber(0)
        tile.draw(win)
        tiletext.draw(win)
        if dir == 1:
            for i in range(int(tiles * tim * 30)):
                tile.move(0, -self.side / (tim * 30))
                tiletext.move(0, -self.side / (tim * 30))
                time.sleep(tim / 30)
        elif dir == 2:
            for i in range(int(tiles * tim * 30)):
                tile.move(self.side / (tim * 30), 0)
                tiletext.move(self.side / (tim * 30), 0)
                time.sleep(tim / 30)
        elif dir == 3:
            for i in range(int(tiles * tim * 30)):
                tile.move(0, self.side / (tim * 30))
                tiletext.move(0, self.side / (tim * 30))
                time.sleep(tim / 30)
        elif dir == 4:
            for i in range(int(tiles * tim * 30)):
                tile.move(-self.side / (tim * 30), 0)
                tiletext.move(-self.side / (tim * 30), 0)
                time.sleep(tim / 30)
        tile.undraw()
        tiletext.undraw()
        del tile
        del tiletext


class Grid:
    def __init__(self, x, y, side, win):
        self.side = side
        self.x = x
        self.y = y
        self.win = win
        self.bigrect = Rectangle(Point(x + side / 2 + 10, y + side / 2 + 10),
                                 Point(x - side / 2 - 10, y - side / 2 - 10))
        self.bigrect.setFill(color_rgb(150, 150, 150))
        self.tiles = [[] for i in range(4)]
        for i in range(4):
            for j in range(4):
                self.tiles[i].append(
                    Tile(x - 1.5 * side / 4 + i * side / 4, y - 1.5 * side / 4 + j * side / 4, 0, side / 4 - 5,
                         self.win))

    def draw(self):
        self.bigrect.draw(self.win)
        for i in range(4):
            for j in range(4):
                self.tiles[j][i].draw()

    def updateTile(self, i, j, number):
        self.tiles[i][j].changeNumber(number)

    def updateGrid(self, arr):
        for i in range(4):
            for j in range(4):
                self.tiles[j][i].changeNumber(arr[i][j])
        update()

    def animateGridTile(self, i, j, tiles, dir, time):
        self.tiles[j][i].moveanimation(tiles, dir, time, self.win)

    def animateGrid(self, arh, ar, arb, dir, tim):
        art = [[] for i in range(4)]
        artt = [[] for i in range(4)]
        for i in range(4):
            for j in range(4):
                artt[i].append([])
        for i in range(4):
            for j in range(4):
                art[i].append(
                    Tile(self.tiles[i][j].x, self.tiles[i][j].y, self.tiles[i][j].number, self.tiles[i][j].side,
                         self.win))
                if art[i][j].number != 0:
                    art[i][j].draw()
                self.tiles[i][j].changeNumber(0)
        for h in range(int(tim * 30)):
            up = False
            for i in range(4):
                for j in range(4):
                    if dir == 1 and ar[i][j]:#sliding animation
                        art[j][i].move(0, -(self.side / 4 - 5) / (tim * 30))
                        up = True
                    elif dir == 2 and ar[i][j]:
                        art[i][j].move((self.side / 4 - 5) / (tim * 30), 0)
                        up = True
                    elif dir == 3 and ar[i][j]:
                        art[j][i].move(0, (self.side / 4 - 5) / (tim * 30))
                        up = True
                    elif dir == 4 and ar[i][j]:
                        art[i][j].move(-(self.side / 4 - 5) / (tim * 30), 0)
                        up = True
                    if arb[i][j] and h<(tim/2 * 30):#doubling animation
                        artt[i][j].append(Tile(self.tiles[i][j].x, self.tiles[i][j].y, arh[j][i], self.tiles[i][j].side + h / tim * 2, self.tiles[i][j].win))
                        artt[i][j][h].draw()
                        up = True
                    elif arb[i][j]:
                        artt[i][j][int(tim * 30)-h].undraw()
                        up = True
            if up:
                update(30)
        for i in range(4):
            for j in range(4):
                art[i][j].undraw()
                if arb[i][j]: artt[i][j][0].undraw()
        del art
        del artt
    def animateGridDouble(self, arb, tim):
        artt = [[] for i in range(4)]
        up = False
        for i in range(4):
            for j in range(4):
                artt[i].append([])
        for h in range(int(tim / 2 * 30)):
            for i in range(4):
                for j in range(4):
                    if arb[i][j]:
                        artt[i][j].append(Tile(self.tiles[i][j].x, self.tiles[i][j].y, self.tiles[i][j].number, self.tiles[i][j].side + h / tim * 2, self.tiles[i][j].win))
                        artt[i][j][h].draw()
                        up=True
            if up: update(30)
        for h in range(int(tim / 2 * 30) - 1, -1, -1):
            for i in range(4):
                for j in range(4):
                    if arb[i][j]:
                        artt[i][j][h].undraw()
                        up = True
            if up: update(30)
        del artt
    def animateSpawn(self,j,i,tim,number):
        ar = []
        for h in range(int(tim*30)):
            ar.append(Tile(self.tiles[i][j].x, self.tiles[i][j].y,number,40+h/(int(tim*30))*(self.tiles[i][j].side-40), self.tiles[i][j].win))
            ar[h].draw()
            update(30)
        for h in range(int(tim*30)):
            ar[h].undraw()
        del ar
