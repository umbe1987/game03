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
    
    DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)
    # draw Tiled map (.tmx) onto screen
    tile_manager.render_tiles(MAP,  DISPLAYSURF)
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
                
        hero.move(level.blocks)
        #collision = pygame.sprite.spritecollide(hero, level.blocks,  False)
        
        # pygame.event.pump() # internally process pygame event handlers
        hero_group.draw(DISPLAYSURF) # draw hero_group onto display Surface
        pygame.display.update(hero.rect) # Update portions (rect or rect list) of the screen
        fpsClock.tick(FPS)
        
