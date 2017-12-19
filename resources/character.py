import pygame
from pygame.locals import *

# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
class Character(pygame.sprite.Sprite):
    """Basic generic character class
    - intended to be inherited from players and enemies in the game -"""

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       super().__init__()

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
 
class Hero(Character):
    def __init__(self,  life):
        super().__init__([255, 0, 0],  5,  5)
        self.life = life
        self.speed = 5
        
    def move(self):
        pygame.event.pump() # internally process pygame event handlers
        key=pygame.key.get_pressed()  #checking pressed keys
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if key[pygame.K_UP]:
            self.rect.move_ip(0, -self.speed)
        if key[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed)
            
