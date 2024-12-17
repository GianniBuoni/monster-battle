from settings import *

class Monster(pygame.sprite.Sprite):
    def __init__(self, name, surface) -> None:
        super().__init__()
        self.image: pygame.Surface = surface
        self.rect = self.image.get_frect(bottomleft = (100, WINDOW_HEIGHT))
        self.name = name

class Opponent(pygame.sprite.Sprite):
    def __init__(self, name, surface, groups) -> None:
        super().__init__(groups)
        self.image: pygame.Surface = surface
        self.rect = self.image.get_frect(midbottom = (WINDOW_WIDTH - 250, 300))
        self.name = name
