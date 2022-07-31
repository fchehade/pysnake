import random
import settings
from entity import Entity


class Enemy(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.surface.fill(settings.BROWN)


class XMovingEnemy(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.surface.fill(settings.COLOR)
        self.direction = True

    def move_sideways(self) -> None:
        if self.direction:
            self.position = (
                self.position[0] + settings.ENEMY_SIZE[0],
                self.position[1],
            )
        else:
            self.position = (
                self.position[0] - settings.ENEMY_SIZE[0],
                self.position[1],
            )

    def move_up(self) -> None:
        self.position = (self.position[0], self.position[1] - settings.ENEMY_SIZE[1])

    def move_down(self) -> None:
        self.position = (self.position[0], self.position[1] + settings.ENEMY_SIZE[1])

    def out_of_bounds_left_right(
        self,
        left_boundary: int,
        right_boundary: int,
    ) -> bool:
        if (
            self.position[0] < left_boundary + settings.ENEMY_SIZE[0]
            or self.position[0] > right_boundary - settings.ENEMY_SIZE[0]
        ):
            return True
        return False


class YMovingEnemy(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.surface.fill(settings.COLOR)
        self.direction = True

    def move_up_and_down(self) -> None:
        if self.direction:
            self.position = (
                self.position[0],
                self.position[1] + settings.ENEMY_SIZE[1],
            )
        else:
            self.position = (
                self.position[0],
                self.position[1] - settings.ENEMY_SIZE[1],
            )

    def out_of_bounds_top_bottom(
        self,
        top_boundary: int,
        bottom_boundary: int,
    ) -> bool:
        if (
            self.position[1] < top_boundary + settings.ENEMY_SIZE[1]
            or self.position[1] > bottom_boundary - settings.ENEMY_SIZE[1]
        ):
            return True
        return False
