import keyboard


def keyreleased(key):#Returns true when key is released
    keypress = False
    while True:
        if keypress and not keyboard.is_pressed(key):
            return True
        elif keyboard.is_pressed(key) and not keypress:
            keypress = True
def arrowkey():#Returns arrow key that was released
    keypress = False
    while True:
        if keyboard.is_pressed("up"):
            keyreleased("up")
            return 1
        elif keyboard.is_pressed("right"):
            keyreleased("right")
            return 2
        elif keyboard.is_pressed("down"):
            keyreleased("down")
            return 3
        elif keyboard.is_pressed("left"):
            keyreleased("left")
            return 4