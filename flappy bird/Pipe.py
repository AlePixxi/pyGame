import pygame
from pygame.constants import *
import random
import gameConstants


class Pipe(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.gap = 100

        self.pipe_down = pygame.image.load(gameConstants.PIPE)
        self.rect_down = self.pipe_down.get_rect()
        self.rect_down.bottom = gameConstants.SCREEN_HEIGHT + self.gap
        self.rect_down.centerx = gameConstants.SCREEN_WIDTH - 80

        self.pipe_up = pygame.transform.flip(self.pipe_down, False, True)
        self.rect_up: pygame.rect.Rect = self.pipe_up.get_rect()
        self.rect_up.top = -self.gap
        self.rect_up.centerx = gameConstants.SCREEN_WIDTH - 80


    def draw (self, surface: pygame.surface.Surface):

        surface.blit(self.pipe_down, self.rect_down)
        surface.blit(self.pipe_up, self.rect_up)