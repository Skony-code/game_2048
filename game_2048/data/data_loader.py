import configparser

config = configparser.ConfigParser()
config.read("game_2048\\data\\settings.ini")
width = config.getint('Window', 'width')
height = config.getint('Window', 'height')
animsped = config.getfloat('Animation','speed')
