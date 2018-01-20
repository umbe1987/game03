try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass
import resources.game as g

if __name__ == "__main__":
    g.game()
    
