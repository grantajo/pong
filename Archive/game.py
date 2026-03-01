from Archive.config import PADDLE_HEIGHT
from Archive.config import SCREEN_HEIGHT
from Archive.config import SCREEN_WIDTH
import pygame

from Archive.config import *

from Archive.player import Paddle
from Archive.ball import Ball

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("2-Player Pong")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74)

        self.player1 = Paddle(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.player2 = Paddle(SCREEN_WIDTH - 25, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.score1 = 0
        self.score2 = 0
        self.running = True

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        keys = pygame.key.get_pressed()
        # Player 1
        if keys[pygame.K_w]:
            self.player1.move_up()
        if keys[pygame.K_s]:
            self.player1.move_down(SCREEN_HEIGHT)
        
        # Player 2
        if keys[pygame.K_UP]:
            self.player2.move_up()
        if keys[pygame.K_DOWN]:
            self.player2.move_down(SCREEN_HEIGHT)

    def update(self):
        self.ball.update(SCREEN_HEIGHT, [self.player1, self.player2])

        if self.ball.rect.left <= 0:
            self.score2 += 1
            self.ball.reset(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        if self.ball.rect.right >= SCREEN_WIDTH:
            self.score1 += 1
            self.ball.reset(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def draw(self):
        self.screen.fill(BLACK)

        for y in range(0, SCREEN_HEIGHT, 15):
            pygame.draw.line(
                self.screen, 
                WHITE, 
                (SCREEN_WIDTH // 2, y), 
                (SCREEN_WIDTH // 2, y + 10), 
                2
                )

            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            self.ball.draw(self.screen)

            score_text = self.font.render(f"{self.score1} {self.score2}", True, WHITE)
            self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))

            pygame.display.flip()

            def run(self):
                while self.running:
                    self.handle_input()
                    self.update()
                    self.draw()
                    self.clock.tick(FPS)

                pygame.quit()

