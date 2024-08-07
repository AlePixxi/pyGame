import pygame
from pygame.constants import *
from pygame.sprite import AbstractGroup
import gameConstants



class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.sprite_num = gameConstants.PLAYER_SPRITES[1]
        self.falling_sprite = gameConstants.PLAYER_SPRITES[0]
        self.jumping_sprite = gameConstants.PLAYER_SPRITES[2]

        self.vertical_speed = 10
        self.image = pygame.image.load(self.sprite_num)

        self.falling_image = pygame.transform.rotate(pygame.image.load(self.falling_sprite), -15)
        self.jumpig_image = pygame.transform.rotate(pygame.image.load(self.jumping_sprite), 15)

        self.rect = self.image.get_rect()
        self.rect.center = (gameConstants.SCREEN_WIDTH/2-100, gameConstants.SCREEN_HEIGHT/2)

        self.vel = 0
        self.gravity = .5
        self.jump_speed = 10

    def jump(self):
        self.vel = -self.jump_speed

    def draw(self, surface: pygame.surface.Surface):

        self.rect.centery += self.vel
        self.vel += self.gravity

        if self.vel > 0:
            self.image = self.falling_image
        elif self.vel < 0:
            self.image = self.jumpig_image


        surface.blit(self.image, self.rect)