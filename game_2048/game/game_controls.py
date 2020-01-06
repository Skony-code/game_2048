import keyboard


def key_released(key):
    # Returns true when key is released
    keypress = False
    while True:
        if keypress and not keyboard.is_pressed(key):
            return True
        elif keyboard.is_pressed(key) and not keypress:
            keypress = True


def arrow_key():
    # Returns number assigned to an arrow key that was released
    keypress = False
    while True:
        if keyboard.is_pressed("up"):
            key_released("up")
            return 1
        elif keyboard.is_pressed("right"):
            key_released("right")
            return 2
        elif keyboard.is_pressed("down"):
            key_released("down")
            return 3
        elif keyboard.is_pressed("left"):
            key_released("left")
            return 4
