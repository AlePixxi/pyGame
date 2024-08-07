import pygame
from pygame.constants import *
import gameConstants


class Background(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.base = pygame.transform.scale(pygame.image.load(gameConstants.BASE), (gameConstants.SCREEN_WIDTH, gameConstants.SCREEN_HEIGHT-500))

        self.background = pygame.transform.scale(pygame.image.load(gameConstants.BACKGROUND), (gameConstants.SCREEN_WIDTH, gameConstants.SCREEN_HEIGHT))
        self.posBack = 0
        self.posBase = 0

    def draw(self, surface: pygame.surface.Surface):

            surface.blit(self.background, (self.posBack,0))
            surface.blit(self.background, (self.posBack+ gameConstants.SCREEN_WIDTH,0))

            surface.blit(self.base, (self.posBase,gameConstants.SCREEN_HEIGHT-100))
            surface.blit(self.base, (self.posBase+gameConstants.SCREEN_WIDTH,gameConstants.SCREEN_HEIGHT-100))
            
            self.posBack -= gameConstants.SPEED-1.3
            self.posBase -= gameConstants.SPEED

            if (self.posBack <= gameConstants.SCREEN_WIDTH*-1):
                 self.posBack = 0
            if (self.posBase <= gameConstants.SCREEN_WIDTH*-1):
                 self.posBase = 0
            