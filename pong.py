from config import PADDLE_HEIGHT
from config import SCREEN_HEIGHT
from config import SCREEN_WIDTH
from config import PADDLE_SPEED
from config import WHITE
from config import BLACK
from config import FPS
import pygame
import numpy as np

class Paddle(pygame.Rect):
    def __init__(self, x, y):
        self.x = x
        self.speed = PADDLE_SPEED

    def move_up():
        if self.rect.top < 0:
            self.rect.y -= self.speed

    def move_down():
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.y += self.speed

class Ball(pygame.Rect):
    def __init__(self, x, y):
        print()

# Initiate game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2-Player Pong")
clock = pygame.time.Clock()

player1 = Paddle(10, SCREEN_WIDTH // 2 - PADDLE_HEIGHT // 2)
player2 = Paddle(SCREEN_WIDTH - 10, SCREEN_WIDTH // 2 - PADDLE_HEIGHT // 2)
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

score1 = 0
score2 = 0
running = True
dt = 0 # Used for speeding up the ball



        



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here

    screen.fill(color=BLACK)

    for y in range(0, SCREEN_HEIGHT, 15):
        pygame.draw.line(
            screen,
            WHITE,
            (SCREEN_WIDTH // 2, y),
            (SCREEN_WIDTH // 2, y + 10)
        )
    

    # Render graphics


    pygame.display.flip()
    clock.tick(FPS)

