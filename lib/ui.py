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
        self.general_idx = {"row": 0, "col": 0}
        self.attack_idx = {"row": 0, "col": 0}
        self.state = "general"

        # grid
        self.rows, self.cols = 2, 2

    def input(self):
        keys = pygame.key.get_just_pressed()
        self.general_idx["row"] = (
            (self.general_idx["row"]
            + int(keys[pygame.K_DOWN])
            - int(keys[pygame.K_UP]))
            % self.rows
        )
        self.general_idx["col"] = (
            (self.general_idx["col"]
            + int(keys[pygame.K_RIGHT])
            - int(keys[pygame.K_LEFT]))
            % self.cols
        )

        # attack menu input needed

        if keys[pygame.K_SPACE]:
            self.state = self.general_options[self.general_idx["col"] * 2 + self.general_idx["row"]]
            print(self.state)

    def quad_select(self, idx, options):
        # bg
        rect = pygame.FRect(self.left, self.top, 400, 200)
        pygame.draw.rect(self.display_surface, "white", rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS["gray"], rect, 4, 4)

        # menu
        for col in range(self.cols):
            for row in range(self.rows):
                x = rect.left + (rect.width / (self.cols * 2)) + (rect.width / self.cols) * col
                y = rect.top + (rect.height / (self.rows * 2)) + (rect.height / self.rows) * row
                i = col * 2 + row
                color = "black" if row == idx["row"] and col == idx["col"] else COLORS["gray"]

                text_surface = self.font.render(options[i], True, color)
                text_rect = text_surface.get_frect(center = (x, y))
                self.display_surface.blit(text_surface, text_rect)

    def update(self):
        self.input()

    def draw(self):
        match self.state:
            case "general": self.quad_select(self.general_idx, self.general_options)
            case "attack": self.quad_select(self.attack_idx, self.monster.abilities)
