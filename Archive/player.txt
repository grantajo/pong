from pygame.key import ScancodeWrapper
from Archive.config import PADDLE_SPEED
from Archive.config import PADDLE_HEIGHT
from Archive.config import PADDLE_WIDTH
from Archive.config import SCREEN_HEIGHT

import pygame

from Archive.config import *

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image - pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.speed = PADDLE_SPEED

    

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed

    def move_down(self, screen_height):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed


    def draw(self, surface):
        surface.blit(self.image, self.rect)
        