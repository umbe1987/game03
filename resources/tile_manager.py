import pytmx,  pygame
from pytmx.util_pygame import load_pygame

# adapted from https://www.reddit.com/r/pygame/comments/2oxixc/pytmx_tiled/cmrvgz4/
def manage_tiles(filename,  screen):
    tmx_data = load_pygame(filename)
    if tmx_data.background_color:
        screen.fill(pygame.Color(tmx_data.background_color))

    # iterate over all the visible layers, then draw them
    # according to the type of layer they are.
    for i, layer in enumerate(tmx_data.visible_layers):

        # draw map tile layers
        if isinstance(layer, pytmx.TiledTileLayer):
            # groups that will  contain blocks and background surfaces
            block_group = pygame.sprite.Group()
            background_group = pygame.sprite.Group()
            # iterate over the tiles in the layer
            for x, y, image in layer.tiles():
                screen.blit(image, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
                # if layer is blocks, add it to block group
                if layer.name == 'blocks':
                    block = pygame.sprite.Sprite()
                    block.image = tmx_data.get_tile_image(x, y, i)
                    block.rect = block.image.get_rect()
                    block_group.add(block)
                # if layer is background, add it to background group
                elif  layer.name == 'background':
                    background = pygame.sprite.Sprite()
                    background.image = tmx_data.get_tile_image(x, y, i)
                    background.rect = background.image.get_rect()
                    background_group.add(background)
                    
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
                
    return block_group,  background_group
