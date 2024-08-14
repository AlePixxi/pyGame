import pygame
from pygame.constants import *
import gameConstants
import sys
import random

from tileset import Tileset
from world import World


class Game:

    def __init__(self) -> None:
        self.fontBig = pygame.font.SysFont("Verdana", 60)
        self.fontSmall = pygame.font.SysFont("Verdana", 24)

        self.gameover = self.fontBig.render("Game Over", True, gameConstants.BLACK)

        self.DISPLAYSURF = pygame.display.set_mode((gameConstants.SCREEN_WIDTH, gameConstants.SCREEN_HEIGHT))
        self.DISPLAYSURF.fill(gameConstants.BLACK)

        pygame.display.set_caption("TopDown Fantasy")

        self.framePerSec = pygame.time.Clock()
        self.tileset = Tileset()
        self.world = World()
        


    def _checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    

    def update(self):
        posX = 0
        while (True):
            self._checkEvents()
            self.DISPLAYSURF.fill(gameConstants.BLACK)

            #cliffAS
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[0], (0, 0))
            #cliffB
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[1], (32, 32))
            #cliffAD
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[2], (32*2, 32*2))
            #cliffD
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[3], (32*3, 32*3))
            #cliffC
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[4], (32*4, 32*4))
            #cliffS
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[5], (32*5, 32*5))
            #cliffBS
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[6], (32*6, 32*6))
            #CliffB
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[7], (32*7, 32*7))
            #CliffBD
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[8], (32*8, 32*8))
            #CliffUpAS
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[9], (32*9, 32*9))
            #CliffUpAD
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[10], (32*10, 32*10))
            #CliffUpBS
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[12], (32*11, 32*11))
            #CliffUpBD
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[13], (32*12, 32*12))
            #CliffGrass1
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[15], (32*13, 32*13))
            #CliffGrass2
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[16], (32*14, 32*14))
            #CliffGrass3
            self.DISPLAYSURF.blit(self.tileset.cliff_tiles[17], (32*15, 32*15))


            self.world.draw("background", self.DISPLAYSURF, "cliff")
            self.world.draw("water", self.DISPLAYSURF, "water")

            pygame.display.update()
            self.framePerSec.tick(60)

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.update()