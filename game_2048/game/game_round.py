from random import randint
from copy import deepcopy
from msvcrt import getch
def end(arr):
    ar=deepcopy(arr)
    for i in range(len(ar) - 1):
        for j in range(len(ar[0]) - 1):
            if(ar[i][j]==ar[i + 1][j] or ar[i][j]==ar[i][j + 1]):
                return False
    return True
def addrandomTile(arr):
    ar = deepcopy(arr)
    x = sum(row.count(0) for row in ar)
    y = randint(0,x)
    z = 0;
    for i in range(len(ar)):
        for j in range(len(ar[0])):
            if ar[i][j] == 0:
                z +=1
                if z==y:
                    if randint(0,1)==1:
                        ar[i][j]=2
                        return ar
                    else:
                        ar[i][j]=4
                        return ar

def move(arr, direction=1):
    ar = deepcopy(arr)
    if(direction==1):
        for h in range(3):
            for i in range(1,4):
                for j in range(4):
                    if ar[i - 1][j]==0:
                        ar[i - 1][j]=ar[i][j]
                        ar[i][j]=0
                    elif ar[i - 1][j]==ar[i][j]:
                        ar[i - 1][j]*=2
                        ar[i][j]=0

    elif(direction==2):
        for h in range(3):
            for i in range(1,4):
                for j in range(4):
                    if ar[i - 1][j]==0:
                        ar[i - 1][j]=ar[i][j]
                        ar[i][j]=0
                    elif ar[i - 1][j]==ar[i][j]:
                        ar[i - 1][j]*=2
                        ar[i][j]=0
    elif(direction==3):
        for h in range(3):
            for i in range(1,4):
                for j in range(4):
                    if ar[i - 1][j]==0:
                        ar[i - 1][j]=ar[i][j]
                        ar[i][j]=0
                    elif ar[i - 1][j]==ar[i][j]:
                        ar[i - 1][j]*=2
                        ar[i][j]=0
    elif(direction==4):
        for h in range(3):
            for i in range(1,4):
                for j in range(4):
                    if ar[i - 1][j]==0:
                        ar[i - 1][j]=ar[i][j]
                        ar[i][j]=0
                    elif ar[i - 1][j]==ar[i][j]:
                        ar[i - 1][j]*=2
                        ar[i][j]=0
    return ar

def round():
    arr = [[0]*4 for i in range(4)]
    ifend = False
    arr2 = addrandomTile(arr)
    arr = deepcopy(arr2)
    while not ifend:
        arr2=addrandomTile(arr)
        arr=deepcopy(arr2)
        ifend = end(arr)
        print(arr)
        while(arr2 == arr):
            arr2=move(arr,1)
        print(arr)
        arr = deepcopy(arr2)
        print(arr)

