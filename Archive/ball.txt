from Archive.config import SCREEN_HEIGHT
from Archive.config import BALL_INIT_SPEED
from Archive.config import BALL_SIZE
import pygame

from Archive.config import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = BALL_INIT_SPEED
        self.speed_y = BALL_INIT_SPEED

    def update(self, screen_height, paddles):
        # Move ball
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top/bottom
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1
        
        # Bounce off paddles
        for paddles in paddles:
            if self.rect.colliderect(paddle.rect):
                self.speed_x *= -1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.speed_x = BALL_INIT_SPEED
        self.speed_y = BALL_INIT_SPEED

    