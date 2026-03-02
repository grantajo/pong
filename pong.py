from config import *
import pygame
import numpy as np
from ball import Ball
from player import Paddle
    

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player1 = Paddle(10, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2)
        self.player2 = Paddle(SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2)
        ball_starting_angle = np.random.uniform(-np.pi / 4, np.pi / 4)
        ball_starting_direction = np.array([np.cos(ball_starting_angle), np.sin(ball_starting_angle)])
        if np.random.rand() < 0.5:
            ball_starting_direction[0] *= -1
        self.ball = Ball(
            SCREEN_WIDTH / 2, 
            SCREEN_HEIGHT / 2, 
            ball_starting_direction,
            BALL_INIT_SPEED,
        )
        self.score1 = 0
        self.score2 = 0
        self.font = pygame.font.Font(None, 74)
        

    def inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        
        keys = pygame.key.get_pressed()
        # Player 1
        if keys[pygame.K_w]:
            self.player1.move_up()
        if keys[pygame.K_s]:
            self.player1.move_down()

        # Player 2
        if keys[pygame.K_UP]:
            self.player2.move_up()
        if keys[pygame.K_DOWN]:
            self.player2.move_down()

    def update(self):
        self.ball.update([self.player1, self.player2])

        # Score updates
        if self.ball.rect.left <= 0:
            self.score2 += 1
            self._reset_ball()
        if self.ball.rect.right >= SCREEN_WIDTH:
            self.score1 += 1
            self._reset_ball()

    def _reset_ball(self):
        angle = np.random.uniform(-np.pi / 4, np.pi / 4)
        direction = np.array([np.cos(angle), np.sin(angle)])
        if np.random.rand() < 0.5:
            direction[0] *= -1
        self.ball = Ball(
            SCREEN_WIDTH / 2, 
            SCREEN_HEIGHT / 2, 
            direction,
            BALL_INIT_SPEED,
        )

    def render(self):
        # Render background
        self.screen.fill(color=BLACK)

        # Render center line
        for y in range(0, SCREEN_HEIGHT, 15):
            pygame.draw.line(
                self.screen,
                WHITE,
                (SCREEN_WIDTH / 2, y),
                (SCREEN_WIDTH / 2, y + 10)
            )

        # Render players and ball
        pygame.draw.rect(self.screen, WHITE, self.player1.rect)
        pygame.draw.rect(self.screen, WHITE, self.player2.rect)
        pygame.draw.ellipse(self.screen, WHITE, self.ball.rect)

        # Render scores
        
        score_text = self.font.render(f"{self.score1}  {self.score2}", True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2, 10))


    def run(self):
        while True:
            self.inputs()
            self.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
