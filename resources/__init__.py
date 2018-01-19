try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass
import pygame
import os.path

TITLE = '''Game 03'''
FPS = 30 # frames per second setting
WIN_WIDTH = 640 # in pixel
WIN_HEIGHT = 480 # in pixel
SCREEN_SIZE = (WIN_WIDTH, WIN_HEIGHT)
DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)
MAP = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'map', 'map01.tmx')
