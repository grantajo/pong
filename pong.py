from config import *
import pygame
import numpy as np

class Paddle(pygame.Rect):
    def __init__(self, x, y):
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.speed = PADDLE_SPEED
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

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

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    

        

# Initiate game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2-Player Pong")
clock = pygame.time.Clock()

player1 = Paddle(10, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2)
player2 = Paddle(SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2)
ball_starting_direction = np.random.randn(2)
ball = Ball(
    SCREEN_WIDTH / 2, 
    SCREEN_HEIGHT / 2, 
    ball_starting_direction,
    BALL_INIT_SPEED,
)

score1 = 0
score2 = 0
running = True
dt = 0 # Used for speeding up the ball

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Update ball speed
    ball.speed = min(ball.speed + dt * BALL_ACCEL, BALL_MAX_SPEED)
    ball.speed_x = ball.direction[0] * ball.speed
    ball.speed_y = ball.direction[1] * ball.speed
    ball.rect.x += ball.speed_x
    ball.rect.y += ball.speed_y
    ball.top_bottom_bounce()
    ball.paddle_bounce([player1, player2])

    # Handle Inputs
    keys = pygame.key.get_pressed()
    # Player 1
    if keys[pygame.K_w]:
        player1.move_up()
    if keys[pygame.K_s]:
        player1.move_down()

    # Player 2
    if keys[pygame.K_UP]:
        player2.move_up()
    if keys[pygame.K_DOWN]:
        player2.move_down()

    # Score updates
    if ball.rect.left <= 0:
        score2 += 1
        ball = Ball(
            SCREEN_WIDTH / 2, 
            SCREEN_HEIGHT / 2, 
            np.random.randn(2),
            BALL_INIT_SPEED,
        )
        dt = 0
    if ball.rect.right >= SCREEN_WIDTH:
        score1 += 1
        ball = Ball(
            SCREEN_WIDTH / 2, 
            SCREEN_HEIGHT / 2, 
            np.random.randn(2),
            BALL_INIT_SPEED,
        )
        dt = 0

    screen.fill(color=BLACK)

    for y in range(0, SCREEN_HEIGHT, 15):
        pygame.draw.line(
            screen,
            WHITE,
            (SCREEN_WIDTH / 2, y),
            (SCREEN_WIDTH / 2, y + 10)
        )

    # Render objects
    player1.draw(screen)
    player2.draw(screen)
    ball.draw(screen)

    pygame.display.flip()
    dt = clock.tick(FPS) / 1000

