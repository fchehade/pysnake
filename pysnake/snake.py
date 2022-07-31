import pygame
import settings


class Snake:
    def __init__(self) -> None:
        self.surface = pygame.Surface((settings.SNAKE_SIZE))
        self.surface.fill(settings.GREEN)
        self.head: tuple[int, int] = (settings.WIDTH // 2, settings.HEIGHT // 2)
        self.direction: tuple[int, int] = (settings.SNAKE_SIZE[0], 0)

    def update_position(self):
        self.head = (
            self.head[0] + self.direction[0],
            self.head[1] + self.direction[1],
        )

    def move_up(self):
        if self.direction != (0, settings.SNAKE_SIZE[1]):
            self.direction = (0, -settings.SNAKE_SIZE[1])

    def move_down(self):
        if self.direction != (0, -settings.SNAKE_SIZE[1]):
            self.direction = (0, settings.SNAKE_SIZE[1])

    def move_left(self):
        if self.direction != (settings.SNAKE_SIZE[0], 0):
            self.direction = (-settings.SNAKE_SIZE[0], 0)

    def move_right(self):
        if self.direction != (-settings.SNAKE_SIZE[0], 0):
            self.direction = (settings.SNAKE_SIZE[0], 0)

    def collided(self, other) -> bool:
        return self.head == other

    def out_of_bounds(
        self,
        left_boundary: int,
        right_boundary: int,
        top_boundary: int,
        bottom_boundary: int,
    ) -> bool:
        if (
            self.head[0] < left_boundary
            or self.head[0] > right_boundary
            or self.head[1] < top_boundary
            or self.head[1] > bottom_boundary
        ):
            return True
        return False
