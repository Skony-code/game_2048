import configparser

config = configparser.ConfigParser()
config.read("C:\\Users\\mateu\\PycharmProjects\\game_2048\\game_2048\\data\\settings.ini")
width = config.getint('Window', 'width')
height = config.getint('Window', 'height')
