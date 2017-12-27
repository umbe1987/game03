import pytmx,  pygame
from pytmx.util_pygame import load_pygame
from resources import *

# adapted from https://www.reddit.com/r/pygame/comments/2oxixc/pytmx_tiled/cmrvgz4/
def render_tiles(filename,  screen):
    tmx_data = load_pygame(filename)
    
    # if Tiled map has no background color set, make it black
    background_color = (0, 0, 0)
    screen.fill(background_color)
    
    if tmx_data.background_color:
        background_color = pygame.Color(tmx_data.background_color)
        screen.fill(background_color)

    # iterate over all the visible layers, then draw them
    # according to the type of layer they are.
    for i, layer in enumerate(tmx_data.visible_layers):

        # draw map tile layers
        if isinstance(layer, pytmx.TiledTileLayer):
            # iterate over the tiles in the layer
            for x, y, image in layer.tiles():
                screen.blit(image, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
                    
        # draw object layers
        elif isinstance(layer, pytmx.TiledObjectGroup):

            # iterate over all the objects in the layer
            for obj in layer:

                # some object have an image
                if obj.image:
                    screen.blit(obj.image, (obj.x, obj.y))

        # draw image layers
        elif isinstance(layer, pytmx.TiledImageLayer):
            if layer.image:
                screen.blit(layer.image, (0, 0))
                
    return background_color

class Level(pygame.sprite.Sprite):
    """Level composed either by blocks (collidant) and background
    - to use in conjunction with Tiled maps and pytmx -"""
    
    def __init__(self,  filename):
        self.filename = filename
        self.blocks = self.manage_tiles(self.filename,  type = 'blocks')
        self.background = self.manage_tiles(self.filename,  type = 'background')
        
    def manage_tiles(self,  filename,  type = None):
        tmx_data = load_pygame(filename)
        # groups that will  contain blocks and background surfaces
        group = pygame.sprite.Group()
        # iterate over all the visible layers of type Tile
        for i, layer in enumerate(tmx_data.visible_layers):
            if isinstance(layer, pytmx.TiledTileLayer):
                # iterate over the tiles in the layer
                for x, y, image in layer.tiles():
                    # save blocks to group
                    if type == 'blocks' and layer.name == 'blocks':
                        block = pygame.sprite.Sprite()
                        block.image = tmx_data.get_tile_image(x, y, i)
                        block.rect = block.image.get_rect()
                        block.rect.move_ip(x * tmx_data.tilewidth, y * tmx_data.tileheight)
                        group.add(block)
                    # save background to group
                    elif type == 'background' and layer.name == 'background':
                        background = pygame.sprite.Sprite()
                        background.image = tmx_data.get_tile_image(x, y, i)
                        background.rect = background.image.get_rect()
                        background.rect.move_ip(x * tmx_data.tilewidth, y * tmx_data.tileheight)
                        group.add(background)
        return group
        
