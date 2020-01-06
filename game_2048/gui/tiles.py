from game_2048.lib.graphics import Rectangle, Text, Point, color_rgb, update

def color(number):
    # color() function returns color for a given number
    # this is used in assigning each Tile a color according to its number
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

class Score:
    # represents score display
    def __init__(self, x, y, win, size):
        # x,y are coordinates of the center of a Score text
        # size must be an integer value between 7 and 36
        # win is Graphic Window in which the Score is displayed
        self.text = Text(Point(x,y), 'Score: ')
        self.text.setSize(size)
        self.text.draw(win)
    def change(self,number):
        # changes displayed text to a given number
        self.text.setText('Score: '+str(number))
        update()

class Tile:
    # represents single Tile
    def __init__(self, x, y, number, side, win):
        # x,y are coordinates of the center of a Tile
        # number is the number displayed on a Tile
        # side is the length of the Tile's side
        # win is Graphic Window in which the Tile is displayed
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
        # draws the Tile
        self.rect.draw(self.win)
        if self.number == 0:
            self.text.setText("")
        self.text.draw(self.win)

    def change_number(self, number):
        # changes number displayed on the Tile as well as its color
        # if the number is 0 no number is displayed on the Tile
        self.number = number
        if self.number != 0:
            self.text.setText(str(number))
        else:
            self.text.setText("")
        self.rect.setFill(color(number))

    def move(self, x, y):
        # moves the Tile x pixels in x direction and y pixels in y direction
        self.rect.move(x, y)
        self.text.move(x, y)

    def undraw(self):
        # undraws the Tile
        self.rect.undraw()
        self.text.undraw()


class Grid:
    # represents 2048 board's graphics
    def __init__(self, x, y, side, win):
        # x,y are coordinates of the center of the board
        # side is the length of the side of the board
        # win is Graphic Window in which the board is displayed
        self.side = side
        self.x = x
        self.y = y
        self.win = win
        # creates gray rectangle as  background for the 2d Tile table
        self.bigrect = Rectangle(Point(x + side / 2 + 10, y + side / 2 + 10), Point(x - side / 2 - 10, y - side / 2 - 10))
        self.bigrect.setFill(color_rgb(150, 150, 150))

        # creates 2d array of Tiles
        self.tiles = [[] for i in range(4)]
        for i in range(4):
            for j in range(4):
                self.tiles[i].append(
                    Tile(x - 1.5 * side / 4 + i * side / 4, y - 1.5 * side / 4 + j * side / 4, 0, side / 4 - 5,
                         self.win))

    def draw(self):
        # draws the board(who could expect that ???)
        self.bigrect.draw(self.win)
        for i in range(4):
            for j in range(4):
                self.tiles[j][i].draw()

    def update(self, arr):
        # changes the numbers displayed on the tiles on the board to the ones provided in arr[][]
        for i in range(4):
            for j in range(4):
                self.tiles[j][i].change_number(arr[i][j])
        update()

    def animate(self, ar_numbers, does_it_slides, does_it_doubles, dir, sliding_time, doubling_time):
        # animates the board
        # animation is done according to the two 2d bool array- does_it_slides and does_it_doubles
        # dir is a direction in which Tiles are supposed to move
        # sliding_time and doubling_time are animation times
        ar_slide = [[] for i in range(4)]
        ar_double = [[] for i in range(4)]
        for i in range(4):
            for j in range(4):
                ar_double[i].append([])
        for i in range(4):
            for j in range(4):
                ar_slide[i].append(
                    Tile(self.tiles[i][j].x, self.tiles[i][j].y, self.tiles[i][j].number, self.tiles[i][j].side,
                         self.win))
                if ar_slide[i][j].number != 0:
                    ar_slide[i][j].draw()
                self.tiles[i][j].change_number(0)
        for h in range(int(sliding_time * 30)):
            up = False
            for i in range(4):
                for j in range(4):
                    # sliding animation
                    if dir == 1 and does_it_slides[i][j]:
                        ar_slide[j][i].move(0, -(self.side / 4 - 5) / (sliding_time * 30))
                        up = True
                    elif dir == 2 and does_it_slides[i][j]:
                        ar_slide[i][j].move((self.side / 4 - 5) / (sliding_time * 30), 0)
                        up = True
                    elif dir == 3 and does_it_slides[i][j]:
                        ar_slide[j][i].move(0, (self.side / 4 - 5) / (sliding_time * 30))
                        up = True
                    elif dir == 4 and does_it_slides[i][j]:
                        ar_slide[i][j].move(-(self.side / 4 - 5) / (sliding_time * 30), 0)
                        up = True
                    # doubling animation
                    if does_it_doubles[i][j] and h <= (doubling_time / 2 * 30) and doubling_time != 0:
                        ar_double[i][j].append(Tile(self.tiles[i][j].x, self.tiles[i][j].y, ar_numbers[j][i],
                                               self.tiles[i][j].side + h / doubling_time * 2, self.tiles[i][j].win))
                        ar_double[i][j][h].draw()
                        up = True
                    elif does_it_doubles[i][j] and h < (doubling_time * 30) and doubling_time != 0:
                        if doubling_time == sliding_time and (doubling_time / 2 * 30) % 2 == 1:
                            b = 1
                        else:
                            b = 0
                        ar_double[i][j][int(doubling_time * 30) - h + b].undraw()
                        up = True
            if up:
                update(30)
        for i in range(4):
            for j in range(4):
                ar_slide[i][j].undraw()
                if does_it_doubles[i][j] and doubling_time > 0: ar_double[i][j][1].undraw()
                if does_it_doubles[i][j] and doubling_time > 0: ar_double[i][j][0].undraw()
        del ar_slide
        del ar_double

    def animate_spawn(self, j, i, tim, number):
        # animates spawn of a new Tile with number in j,i coordinates in tim time
        ar = []
        for h in range(int(tim * 30)):
            ar.append(Tile(self.tiles[i][j].x, self.tiles[i][j].y, number,
                           40 + h / (int(tim * 30)) * (self.tiles[i][j].side - 40), self.tiles[i][j].win))
            ar[h].draw()
            update(30)
        for h in range(int(tim * 30)):
            ar[h].undraw()
        del ar
