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
    background_color = tile_manager.render_tiles(MAP,  DISPLAYSURF)
    background_surf = pygame.Surface((32, 32))
    background_surf.fill(background_color)
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
        
        # check if hero is overlapping level.background
        background_overlap = pygame.sprite.groupcollide(hero_group,  level.background, False, False)
        
        # if hero is overlaping level.background, blit it on hero position, otherwise blit background_color
        hero_pos = hero.rect.copy() # store hero position before moving
        if background_overlap:
            background_sprite = list(background_overlap.values())[0][0] # 32x32 tile
            DISPLAYSURF.blit(background_sprite.image, background_sprite.rect)
        else:
            DISPLAYSURF.blit(background_surf, background_surf.get_rect())
            
        dirty_rects.append(hero_pos)
        
        hero.move(level.blocks)
        dirty_rects.append(hero.rect)
        
        # pygame.event.pump() # internally process pygame event handlers
        hero_group.draw(DISPLAYSURF) # draw hero_group onto display Surface
        pygame.display.update(dirty_rects) # Update portions (rect or rect list) of the screen
        fpsClock.tick(FPS)
        
