import pygame
from pygame.constants import *

from tileset import Tileset


class World(pygame.sprite.Sprite):

    def __init__(self) -> None:
        self.tileset = Tileset()
        self.backgroundMapPath = "./assets/backgroundMap.txt"
        self.waterMapPath = "./assets/waterMap.txt"

    def draw(self,map_choise:str, surface:pygame.surface.Surface, tileset:str):
        tiles = self.tileset.cliff_tiles

        match(map_choise):
            case "background": map = self.backgroundMapPath
            case "water": map = self.waterMapPath

            case _: None

        

        with open(map, "r") as bM:
            for y,row in enumerate(bM):
                for x,tile in enumerate(row):
                    if tile.isnumeric():
                        match (tileset):
                            case "cliff": tiles = self.tileset.cliff_tiles 
                            case "water": tiles = self.tileset.water_tiles
                            case "path": tiles = self.tileset.path_tiles
                            case "farm": tiles = self.tileset.farmland_tiles
                            case _: tiles = None
                        surface.blit(tiles[int(tile)], (x*32, y*32))
                    elif tile == "x":
                        match (tileset):
                            case "cliff": tiles = self.tileset.cliff_tiles 
                            case "water": tiles = self.tileset.water_tiles
                            case "path": tiles = self.tileset.path_tiles
                            case "farm": tiles = self.tileset.farmland_tiles
                            case _: tiles = None
                        surface.blit(tiles[10], (x*32, y*32))
                    elif tile == "d":
                        match (tileset):
                            case "cliff": tiles = self.tileset.cliff_tiles 
                            case "water": tiles = self.tileset.water_tiles
                            case "path": tiles = self.tileset.path_tiles
                            case "farm": tiles = self.tileset.farmland_tiles
                            case _: tiles = None
                        surface.blit(tiles[12], (x*32, y*32))