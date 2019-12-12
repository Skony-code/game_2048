import configparser

config = configparser.ConfigParser()
config.read('D:\Pythonpro\game_2048\game_2048\data\settings.ini')
width = config.getint('Window', 'width')
height = config.getint('Window', 'height')
