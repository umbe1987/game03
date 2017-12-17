import pygame,  sys
from pygame.locals import *
import resources.character as character
from resources import *

def game():
    """main function"""
    
    pygame.init()    
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption(TITLE) # set the title in the caption
        
    DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)
    hero = character.Hero(12) # instance of Hero character
    hero_group = pygame.sprite.Group()
    hero_group.add(hero)
    
    hero_group.draw(DISPLAYSURF) # draw hero_group onto display Surface
    pygame.display.update(hero.rect) # update full display Surface to the screen
    
    while True: # main game loop
        for event in pygame.event.get():
            # quit the game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.event.pump()
        pygame.display.update()
        fpsClock.tick(FPS)
        
