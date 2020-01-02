import configparser

config = configparser.ConfigParser()
config.read("game_2048\\data\\settings.ini")
width = config.getint('Window', 'width')
height = config.getint('Window', 'height')
slidetime = config.getfloat('Animation', 'slidetime')
doubletime = config.getfloat('Animation','doubletime')

