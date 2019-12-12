from random import randint
def end(arr = [[0]*4 for i in range(4)]):
    for i in range(len(arr)-1):
        for j in range(len(arr[0])-1):
            if(arr[i][j]==arr[i+1][j] or arr[i][j]==arr[i][j+1]):
                return False
    return True
def addrandomTile(arr = [[0]*4 for i in range(4)]):
    x = sum(row.count(0) for row in arr)
    y = randint(0,x)
    z = 0;
    print(y)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                z +=1
                if z==y:
                    print(arr)
                    if randint(0,1)==1:
                        arr[i][j]=2
                        return arr
                    else:
                        arr[i][j]=4
                        return arr
def round():
    arr = [[0]*4 for i in range(4)]
    while not end(arr):
        arr2=addrandomTile(arr)
        arr=arr2.copy()

