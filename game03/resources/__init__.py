import os.path

TITLE = '''Game 03'''
FPS = 30 # frames per second setting
WIN_WIDTH = 1280 # in pixel
WIN_HEIGHT = 720 # in pixel
SCREEN_SIZE = (WIN_WIDTH, WIN_HEIGHT)
MAP = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'map', 'map01.tmx')
