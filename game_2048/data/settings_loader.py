import configparser

# loading the settings from settings.ini
config = configparser.ConfigParser()
config.read("data\\settings.ini")
window_width = config.getint('Window', 'width')
window_height = config.getint('Window', 'height')
sliding_time = config.getfloat('Animation', 'sliding time')
doubling_time = config.getfloat('Animation', 'doubling time')
spawning_time = config.getfloat('Animation', 'spawning time')
grid_side = config.getint('Tiles', 'grid side')
ai = config.getboolean('AI', 'on/off')
