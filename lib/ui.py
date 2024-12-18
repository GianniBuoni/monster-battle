from settings import *

class UI():
    def __init__(self, monster) -> None:
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        self.left = WINDOW_WIDTH / 2
        self.top = WINDOW_HEIGHT / 2 + 100
        self.monster = monster

        # control
        self.general_options = ["attack", "heal", "switch", "escape"]

    def general(self):
        # bg
        rect = pygame.FRect(self.left, self.top, 400, 200)
        pygame.draw.rect(self.display_surface, "white", rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS["gray"], rect, 4, 4)

        # menu
        cols, rows = 2, 2
        for col in range(cols):
            for row in range(rows):
                x = rect.left + (rect.width / 4) + (rect.width / 2) * col
                y = rect.top + (rect.height / 4) + (rect.height / 2) * row
                i = col + 2 * row

                text_surface = self.font.render(self.general_options[i], True, "black")
                text_rect = text_surface.get_frect(center = (x, y))
                self.display_surface.blit(text_surface, text_rect)

    def draw(self):
        self.general()

