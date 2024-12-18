from random import sample
from settings import *

class Monster():
    def get_data(self, name):
        self.element = MONSTER_DATA[name]["element"]
        self.health = self.max_health = MONSTER_DATA[name]["health"]
        self.abilities = sample(list(ABILITIES_DATA.keys()), 4)
        self.name = name

class Player(pygame.sprite.Sprite, Monster):
    def __init__(self, name, surface) -> None:
        super().__init__()
        self.image: pygame.Surface = surface
        self.rect = self.image.get_frect(bottomleft = (100, WINDOW_HEIGHT))
        self.name = name
        self.get_data(name)

class Opponent(pygame.sprite.Sprite, Monster):
    def __init__(self, name, surface, groups) -> None:
        super().__init__(groups)
        self.image: pygame.Surface = surface
        self.rect = self.image.get_frect(midbottom = (WINDOW_WIDTH - 250, 300))
        self.name = name
        self.get_data(name)
