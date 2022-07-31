import pygame
import settings


class Scoreboard:
    def __init__(self) -> None:
        pygame.font.init()
        self.position = (10, 10)
        self.font = pygame.font.SysFont("Calibri", 22)
        self.score = 0
        self.score_text = self.font.render(f"Score: {self.score}", True, settings.WHITE)

    def add_score(self) -> None:
        self.score += 1

    def update_score_text(self) -> None:
        self.score_text = self.font.render(f"Score: {self.score}", True, settings.WHITE)
