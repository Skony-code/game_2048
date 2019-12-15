from random import randint
from copy import deepcopy
from game_2048.game.game_controls import arrowkey
from game_2048.graphics.print_table import printtab

def end(arr):
    ar = deepcopy(arr)
    for i in range(len(ar) - 1):
        for j in range(len(ar[0]) - 1):
            if (ar[i][j] == ar[i + 1][j] or ar[i][j] == ar[i][j + 1]):
                return False
    return True


def addrandomTile(arr):
    ar = deepcopy(arr)
    x = sum(row.count(0) for row in ar)
    y = randint(0, x-1)
    z = -1;
    for i in range(len(ar)):
        for j in range(len(ar[0])):
            if ar[i][j] == 0:
                z += 1
                if z == y:
                    if randint(0, 1) == 1:
                        ar[i][j] = 2
                        return ar
                    else:
                        ar[i][j] = 4
                        return ar


def move(arr, direction=1):
    ar = deepcopy(arr)
    if direction == 1:
        for h in range(3):
            for i in range(1, 4):
                for j in range(4):
                    if ar[i - 1][j] == 0:
                        ar[i - 1][j] = ar[i][j]
                        ar[i][j] = 0
                    elif ar[i - 1][j] == ar[i][j]:
                        ar[i - 1][j] *= 2
                        ar[i][j] = 0

    elif direction == 2:
        for h in range(3):
            for i in range(2, -1, -1):
                for j in range(4):
                    if ar[j][i+1] == 0:
                        ar[j][i+1] = ar[j][i]
                        ar[j][i] = 0
                    elif ar[j][i+1] == ar[j][i]:
                        ar[j][i+1] *= 2
                        ar[j][i] = 0
    elif direction == 3:
        for h in range(3):
            for i in range(2, -1, -1):
                for j in range(4):
                    if ar[i + 1][j] == 0:
                        ar[i + 1][j] = ar[i][j]
                        ar[i][j] = 0
                    elif ar[i + 1][j] == ar[i][j]:
                        ar[i + 1][j] *= 2
                        ar[i][j] = 0
    elif direction == 4:
        for h in range(3):
            for i in range(1, 4):
                for j in range(4):
                    if ar[j][i-1] == 0:
                        ar[j][i-1] = ar[j][i]
                        ar[j][i] = 0
                    elif ar[j][i-1] == ar[j][i]:
                        ar[j][i-1] *= 2
                        ar[j][i] = 0
    return ar

def round():
    arr = [[0] * 4 for i in range(4)]
    ifend = False
    arr2 = addrandomTile(arr)
    arr = deepcopy(arr2)
    while not ifend:
        arr2 = addrandomTile(arr)
        arr = deepcopy(arr2)
        ifend = end(arr)
        printtab(arr)
        print("")
        while (arr2 == arr):
            arr2 = move(arr, arrowkey())
        arr = deepcopy(arr2)
        printtab(arr)
        print("")