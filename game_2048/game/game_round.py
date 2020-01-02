from random import randint
from copy import deepcopy
from game_2048.game.game_controls import arrowkey
from game_2048.graphics.print_table import printtab
from game_2048.graphics.tiles import *
from game_2048.data import  data_loader


def end(ar):
    for i in range(len(ar) - 1):
        for j in range(len(ar) - 1):
            if ar[i][j] == ar[i + 1][j] or ar[i][j] == ar[i][j + 1]:
                return False
    for i in range(len(ar)):
        for j in range(len(ar)):
            if ar[i][j] == 0 or ar[i][j] == 0:
                return False
    for i in range(len(ar) - 1):
        if ar[3][i] == ar[3][i + 1] or ar[i][3] == ar[i + 1][3]:
            return False
    return True


def addrandomTile(ar,grid):
    x = sum(row.count(0) for row in ar)
    y = randint(0, x - 1)
    z = -1
    for i in range(len(ar)):
        for j in range(len(ar[0])):
            if ar[i][j] == 0:
                z += 1
                if z == y:
                    if randint(0, 2) != 1:
                        ar[i][j] = 2
                        grid.animateSpawn(i,j,data_loader.spwntime,2)
                    else:
                        ar[i][j] = 4
                        grid.animateSpawn(i, j, data_loader.spwntime, 4)
    grid.updateGrid(ar)


def move(ar, direction,grid):
    ifdoub= [[False] * 4 for i in range(4)]
    for h in range(3):
        arr = [[False] * 4 for i in range(4)]#creates bool list for moving tiles
        arrr = [[False] * 4 for i in range(4)]  # creates bool list for doubling tiles
        if direction == 1:
            for i in range(1, 4):
                for j in range(4):
                    if ar[i - 1][j] == 0 and ar[i][j]!=0:
                        ar[i - 1][j] = ar[i][j]
                        ar[i][j] = 0
                        ifdoub[i-1][j] = ifdoub[i][j]
                        ifdoub[i][j] = False
                        arr[i][j]=True
                    elif ar[i - 1][j] == ar[i][j] and ar[i][j]!=0 and not ifdoub[i-1][j] and not ifdoub[i][j]:
                        ar[i - 1][j] *= 2
                        ar[i][j] = 0
                        arr[i][j] = True
                        arrr[j][i-1] = True
                        ifdoub[i - 1][j] = True
                        ifdoub[i][j] = False
        elif direction == 2:
            for i in range(2, -1, -1):
                for j in range(4):
                    if ar[j][i + 1] == 0 and ar[j][i]!=0:
                        ar[j][i + 1] = ar[j][i]
                        ar[j][i] = 0
                        ifdoub[j][i + 1] = ifdoub[j][i]
                        ifdoub[j][i] = False
                        arr[i][j] = True
                    elif ar[j][i + 1] == ar[j][i] and ar[j][i]!=0 and not ifdoub[j][i+1] and not ifdoub[j][i]:
                        ar[j][i + 1] *= 2
                        ar[j][i] = 0
                        arr[i][j] = True
                        arrr[i+1][j] = True
                        ifdoub[j][i + 1] = True
                        ifdoub[j][i] = False
        elif direction == 3:
            for i in range(2, -1, -1):
                for j in range(4):
                    if ar[i + 1][j] == 0 and ar[i][j]!=0:
                        ar[i + 1][j] = ar[i][j]
                        ar[i][j] = 0
                        ifdoub[i + 1][j] = ifdoub[i][j]
                        ifdoub[i][j] = False
                        arr[i][j] = True
                    elif ar[i + 1][j] == ar[i][j] and ar[i][j]!=0 and not ifdoub[i+1][j] and not ifdoub[i][j]:
                        ar[i + 1][j] *= 2
                        ar[i][j] = 0
                        arr[i][j] = True
                        arrr[j][i+1] = True
                        ifdoub[i + 1][j] = True
                        ifdoub[i][j] = False
        elif direction == 4:
            for i in range(1, 4):
                for j in range(4):
                    if ar[j][i - 1] == 0 and ar[j][i]!=0:
                        ar[j][i - 1] = ar[j][i]
                        ar[j][i] = 0
                        ifdoub[j][i - 1] = ifdoub[j][i]
                        ifdoub[j][i] = False
                        arr[i][j] = True
                    elif ar[j][i - 1] == ar[j][i] and ar[j][i]!=0 and not ifdoub[j][i-1] and not ifdoub[j][i]:
                        ar[j][i - 1] *= 2
                        ar[j][i] = 0
                        arr[i][j] = True
                        arrr[i-1][j] = True
                        ifdoub[j][i - 1] = True
                        ifdoub[j][i] = False
        grid.animateGrid(ar, arr, arrr, direction, data_loader.slidetime,data_loader.doubletime)
        grid.updateGrid(ar)

def score(ar):
    x=ar[0][0]
    for i in range(4):
        for j in range(4):
            if ar[i][j]>x: x=ar[i][j]
    return x

def round(win, width, height):
    arr = [[0] * 4 for i in range(4)]
    scor = Text(Point(width/2+data_loader.gridside/2+120,40),'Score: ')
    scor.setSize(int(height/30))
    scor.draw(win)
    grid = Grid(width / 2, height / 2, data_loader.gridside,win)
    grid.draw()
    addrandomTile(arr,grid)
    while True:
        addrandomTile(arr,grid)
        arr2 = deepcopy(arr)
        printtab(arr)
        scor.setText('Score: '+str(score(arr)))
        update()
        print(score(arr))
        if end(arr):
            text = Text(Point(width / 2, height / 2), "GAME OVER")
            text.setSize(36)
            text.draw(win)
            update()
            input()
            break
        while arr2 == arr:
            move(arr, arrowkey(),grid)