import pygame
from pygame.constants import *
import gameConstants
import sys
import random

from Player import Player
from background import Background

class Game:

    def __init__(self) -> None:
        self.fontBig = pygame.font.SysFont("Verdana", 60)
        self.fontSmall = pygame.font.SysFont("Verdana", 24)

        self.gameover = self.fontBig.render("Game Over", True, gameConstants.BLACK)

        self.DISPLAYSURF = pygame.display.set_mode((gameConstants.SCREEN_WIDTH, gameConstants.SCREEN_HEIGHT))
        self.DISPLAYSURF.fill(gameConstants.BLACK)

        pygame.display.set_caption("Flap.py Bird")
        pygame.display.set_icon(pygame.image.load(gameConstants.FAVICON))

        self.framePerSec = pygame.time.Clock()

        self.incEvent = pygame.USEREVENT + 1
        pygame.time.set_timer(self.incEvent, 1000)

        self.player = Player()
        self.background = Background()


    def _checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == self.incEvent:
                gameConstants.SPEED += .1

    def update(self):

        while (True):
            self._checkEvents()

            self.DISPLAYSURF.fill(gameConstants.BLACK)
            self.background.draw(self.DISPLAYSURF)
            self.player.draw(self.DISPLAYSURF)

            pygame.display.update()
            self.framePerSec.tick(60)


pygame.init()
game = Game()
game.update()