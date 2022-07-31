import settings
from entity import Entity


class Apple(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.surface.fill(settings.RED)
