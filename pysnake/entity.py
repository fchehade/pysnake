import random
import pygame
import settings


class Entity:
    def __init__(self) -> None:
        self.surface = pygame.Surface((settings.ENTITY_SIZE))
        self.position = self.new_position()

    def new_position(self) -> tuple[int, int]:
        return (
            random.randrange(
                0 + settings.ENTITY_SIZE[0],
                settings.WIDTH - settings.ENTITY_SIZE[0],
                step=settings.ENTITY_SIZE[0],
            ),
            random.randrange(
                0 + settings.ENTITY_SIZE[1],
                settings.HEIGHT - settings.ENTITY_SIZE[1],
                step=settings.ENTITY_SIZE[1],
            ),
        )

    def _generate_new_position(self) -> None:
        self.position = self.new_position()
