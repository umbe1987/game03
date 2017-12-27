import pygame

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
        super().__init__([255, 0, 0], 32, 32)
        self.life = life
        self.speed = 5
        self.dx = 0
        self.dy = 0
        
    def move(self, collidant = pygame.sprite.Group()):
        """move the hero"""
        
        self.dx = 0
        self.dy = 0
        
        pygame.event.pump() # internally process pygame event handlers
        key=pygame.key.get_pressed()  #checking pressed keys
        if key[pygame.K_LEFT]:
            self.dx = -self.speed
            self.rect.move_ip(-self.speed, 0)
        if key[pygame.K_RIGHT]:
            self.dx = +self.speed
            self.rect.move_ip(self.speed, 0)
        if key[pygame.K_UP]:
            self.dy = -self.speed
            self.rect.move_ip(0, -self.speed)
        if key[pygame.K_DOWN]:
            self.dy = +self.speed
            self.rect.move_ip(0, self.speed)
            
        self.collision(collidant)
            
    def collision(self,  collidant = pygame.sprite.Group()):
        """check for collision against pygame.sprite.Group()"""
        
        collision_list = pygame.sprite.spritecollide(self,  collidant,  False)
        
        if collision_list:
            for collision in collision_list:
                # left collision
                if self.dx < 0:
                    self.rect.left = collision.rect.right
                # right collision
                if self.dx > 0:
                    self.rect.right = collision.rect.left
                # top collision
                if self.dy < 0:
                    self.rect.top = collision.rect.bottom
                # bottom collision
                if self.dy > 0:
                    self.rect.bottom = collision.rect.top
