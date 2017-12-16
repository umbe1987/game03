import pygame,  sys
from pygame.locals import *
from resources import *

def game():
    """main function"""
    
    pygame.init()    
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption(TITLE) # set the title in the caption
        
    DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)
    
    while True: # main game loop
        for event in pygame.event.get():
            # quit the game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.event.pump()
        pygame.display.update()
        fpsClock.tick(FPS)
        
