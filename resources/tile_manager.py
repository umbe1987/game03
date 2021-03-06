import pytmx,  pygame
from pytmx.util_pygame import load_pygame
from resources import *

class Level(pygame.sprite.Sprite):
    """Level composed either by blocks (collidant) and background
    - to use in conjunction with Tiled maps and pytmx -"""
    
    def __init__(self,  filename):
        self.filename = filename
        tmx_data = load_pygame(self.filename)
        self.screen = DISPLAYSURF
        
        # store blocks and background tiles in group
        self.blocks = self.manage_tiles(tmx_data,  type = 'blocks')
        self.background_tile = self.manage_tiles(tmx_data,  type = 'background')
        
        # render image layer (as background) first, then object and tile layers
        self.background = self.render_image_lyr(tmx_data, self.screen)
        self.render_tiled_lyr(tmx_data, self.screen)
        self.render_object_lyr(tmx_data, self.screen)
        
    def manage_tiles(self,  tmx_data,  type = None):
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

    # adapted from https://www.reddit.com/r/pygame/comments/2oxixc/pytmx_tiled/cmrvgz4/
    def render_image_lyr(self, tmx_data, screen):
        for layer in tmx_data.visible_layers:
            # draw image layers
            if isinstance(layer, pytmx.TiledImageLayer):
                if layer.image:
                    background = layer
                    screen.blit(background.image, (0, 0))
                    
        return background

    # adapted from https://www.reddit.com/r/pygame/comments/2oxixc/pytmx_tiled/cmrvgz4/
    def render_tiled_lyr(self, tmx_data, screen):
        for layer in tmx_data.visible_layers:
            # draw map tile layers
            if isinstance(layer, pytmx.TiledTileLayer):
                # iterate over the tiles in the layer
                for x, y, image in layer.tiles():
                    screen.blit(image, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
                    
        return
        
    # adapted from https://www.reddit.com/r/pygame/comments/2oxixc/pytmx_tiled/cmrvgz4/
    def render_object_lyr(self, tmx_data, screen):
        for layer in tmx_data.visible_layers:
            # draw object layers
            if isinstance(layer, pytmx.TiledObjectGroup):
                # iterate over all the objects in the layer
                for obj in layer:
                    # some object have an image
                    if obj.image:
                        screen.blit(obj.image, (obj.x, obj.y))
        return
