import pytmx,  pygame
from pytmx.util_pygame import load_pygame

# adapted from https://www.reddit.com/r/pygame/comments/2oxixc/pytmx_tiled/cmrvgz4/
def render_tiles_to_screen(filename,  screen):
    tmx_data = load_pygame(filename)
    if tmx_data.background_color:
        screen.fill(pygame.Color(tmx_data.background_color))

    # iterate over all the visible layers, then draw them
    # according to the type of layer they are.
    for layer in tmx_data.visible_layers:

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
