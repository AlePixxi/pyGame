import pygame
from pygame.sprite import AbstractGroup
from pygame.constants import *


class Tileset(pygame.sprite.Sprite):

    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)

        self.cliff_tile = pygame.image.load("./assets/Tiles/Cliff_Tile.png")
        self.cliff_tile = pygame.transform.scale2x(self.cliff_tile)

        self.farmland_tile = pygame.image.load("./assets/Tiles/FarmLand_Tile.png").convert_alpha()
        self.farmland_tile = pygame.transform.scale2x(self.farmland_tile)

        self.grass_middle = pygame.image.load("./assets/Tiles/Grass_Middle.png").convert_alpha()
        
        self.water_tile = pygame.image.load("./assets/Tiles/Water_Tile.png").convert_alpha()
        self.water_tile = pygame.transform.scale2x(self.water_tile)

        self.path_tile = pygame.image.load("./assets/Tiles/Path_Tile.png").convert_alpha()
        self.path_tile = pygame.transform.scale2x(self.path_tile)
        
        self.path_middle = pygame.image.load("./assets/Tiles/Path_Middle.png").convert_alpha()
        self.water_middle = pygame.image.load("./assets/Tiles/Water_Middle.png").convert_alpha()

        self.cliff_tiles = self.divide_image(self.cliff_tile, 32, 32)
        self.farmland_tiles = self.divide_image(self.farmland_tile, 32, 32)
        self.water_tiles = self.divide_image(self.water_tile, 32, 32)
        self.path_tiles = self.divide_image(self.farmland_tile, 32, 32)

        self.tree = pygame.image.load("./assets/Outdoor decoration/Oak_Tree.png").convert_alpha()
        self.tree = pygame.transform.scale2x(self.tree)


    def get_image_at(self, surface, rectangle, colorkey=None):
        """Copia una porzione di una superficie."""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(surface, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image
    

    def divide_image(self, image, tile_width, tile_height):
        """Divide un'immagine in tile di dimensioni specificate."""
        image_width, image_height = image.get_size()
        tiles = []
        for y in range(0, image_height, tile_height):
            for x in range(0, image_width, tile_width):
                tile = self.get_image_at(image, (x, y, tile_width, tile_height))
                tiles.append(tile)
        return tiles