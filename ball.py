import pygame
import numpy as np

from config import *

class Ball(pygame.Rect):
    def __init__(self, x, y, direction: np.ndarray, speed: float):
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction / np.linalg.norm(direction)
        self.speed = speed
        self.speed_x = self.direction[0] * self.speed
        self.speed_y = self.direction[1] * self.speed
    
    def top_bottom_bounce(self):
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1
            self.direction[1] *= -1

    def paddle_bounce(self, paddles):
        for paddle in paddles:
            if self.rect.colliderect(paddle.rect):
                self.speed_x *= -1
                self.direction[0] *= -1
    
    def update(self, paddles):
        # Update ball
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Check for collisions
        self.top_bottom_bounce()
        self.paddle_bounce(paddles)

    def top_bottom_bounce(self):
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1
            self.direction[1] *= -1

    def paddle_bounce(self, paddles):
        for paddle in paddles:
            if self.rect.colliderect(paddle.rect):
                self.speed_x *= -1
                self.direction[0] *= -1

    def draw(self, surface):
        surface.blit(self.image, self.rect)
