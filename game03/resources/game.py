try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass
import pygame,  sys
from pygame.locals import *
import resources.character as character
import resources.tile_manager as tile_manager
from resources import *

def game():
    """main function"""
    
    pygame.init()    
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption(TITLE) # set the title in the caption
    
    # draw Tiled map (.tmx) onto screen and retain background sprite
    # get blocks and background tiles from Tiled in two distict pygame groups
    level = tile_manager.Level(MAP)
    # instance of Hero character
    hero = character.Hero(12)
    hero_group = pygame.sprite.Group()
    hero_group.add(hero)
    
    hero_group.draw(DISPLAYSURF) # draw hero_group onto display Surface
    pygame.display.update()
    
    while True: # main game loop
        for event in pygame.event.get():
            # quit the game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        # list to store dirty_rects (argument for pygame.display.update())
        dirty_rects = []
        
        hero_pos = hero.rect.copy() # store hero position before moving
        DISPLAYSURF.blit(level.background.image, hero_pos, hero_pos)
        
        dirty_rects.append(hero_pos)
        
        hero.move(level.blocks)
        dirty_rects.append(hero.rect)
        
        # pygame.event.pump() # internally process pygame event handlers
        hero_group.draw(DISPLAYSURF) # draw hero_group onto display Surface
        pygame.display.update(dirty_rects) # Update portions (rect or rect list) of the screen
        fpsClock.tick(FPS)
        
