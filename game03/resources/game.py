try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass
import pygame,  os
from pygame.locals import *
import resources.character as character
from resources import *

# taken from https://github.com/renpytom/rapt-pygame-example/blob/master/main.py
def save_state(x, y):
    """
    Saves the game state.
    """

    with open("state.txt", "w") as f:
        f.write("{} {}".format(x, y))

def load_state():
    try:
        with open("state.txt", "r") as f:
            x, y = f.read().split()
            x = int(x)
            y = int(y)

        return x, y
    except:
        return None, None

def delete_state():

    if os.path.exists("state.txt"):
        os.unlink("state.txt")
        
def game():
    """main function"""
    
    pygame.init()    
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption(TITLE) # set the title in the caption
    
    # inizialize screen with black color background
    screen = pygame.display.set_mode(SCREEN_SIZE)
    
    # instance of Hero character
    hero = character.Hero(12)
    hero_group = pygame.sprite.Group()
    hero_group.add(hero)
    
    hero_group.draw(screen) # draw hero_group onto display Surface
    pygame.display.update()
    
    sleeping = False
    
    # On startup, load state saved by APP_WILLENTERBACKGROUND, and the delete
    # that state.
    x, y = load_state()
    delete_state()

    while True: # main game loop
        # If not sleeping, draw the screen.
        if not sleeping:
            screen.fill((0, 0, 0, 255))
            
            # list to store dirty_rects (argument for pygame.display.update())
            dirty_rects = []
            
            hero_pos = hero.rect.copy() # store hero position before moving
            screen.blit(screen, hero_pos, hero_pos)
            
            dirty_rects.append(hero_pos)
            
            hero.move()
            dirty_rects.append(hero.rect)
            
            # pygame.event.pump() # internally process pygame event handlers
            hero_group.draw(screen) # draw hero_group onto display Surface
            pygame.display.update(dirty_rects) # Update portions (rect or rect list) of the screen
            
        ev = pygame.event.wait()

        # Pygame quit.
        if ev.type == pygame.QUIT:
            break

        # Android back key.
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_AC_BACK:
            break

        elif ev.type == pygame.APP_WILLENTERBACKGROUND:
            # The app is about to go to sleep. It should save state, cancel
            # any timers, and stop drawing the screen until an APP_DIDENTERFOREGROUND
            # event shows up.

            save_state(x, y)

            sleeping = True

        elif ev.type == pygame.APP_DIDENTERFOREGROUND:
            # The app woke back up. Delete the saved state (we don't need it),
            # restore any times, and start drawing the screen again.

            delete_state()
            sleeping = False

            # For now, we have to re-open the window when entering the
            # foreground.
            screen = pygame.display.set_mode(SCREEN_SIZE)
                
        fpsClock.tick(FPS)
    
