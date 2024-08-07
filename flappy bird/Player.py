import pygame
from pygame.constants import *
from pygame.sprite import AbstractGroup
import gameConstants



class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.sprite_num = gameConstants.PLAYER_SPRITES[0]
        self.vertical_speed = 10
        self.image = pygame.image.load(self.sprite_num)
        self.rect = self.image.get_rect()
        self.rect.center = (gameConstants.SCREEN_WIDTH/2-100, gameConstants.SCREEN_HEIGHT/2)


    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.image, self.rect)