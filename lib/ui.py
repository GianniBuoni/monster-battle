from settings import *

class UI():
    def __init__(self, current_monster, player_monsters) -> None:
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        self.left = WINDOW_WIDTH / 2
        self.top = WINDOW_HEIGHT / 2 + 100
        self.monster = current_monster
        self.player_monsters = player_monsters

        # control
        self.general_options = ["attack", "heal", "switch", "escape"]
        self.general_idx = {"row": 0, "col": 0}
        self.attack_idx = {"row": 0, "col": 0}
        self.switch_idx = 0
        self.state = "general"
        self.visible_monsters = 4

        # grid
        self.rows, self.cols = 2, 2

    def input(self):
        keys = pygame.key.get_just_pressed()
        match self.state:
            case "general":
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
                if keys[pygame.K_SPACE]:
                    self.state = self.general_options[self.general_idx["col"] * 2 + self.general_idx["row"]]
                    print(self.state)
            case "switch":
                self.switch_idx = (self.switch_idx + int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])) % self.visible_monsters
        # attack menu input needed

    def quad_select(self, idx, options):
        # bg
        rect = pygame.FRect(self.left, self.top, 400, 200)
        pygame.draw.rect(self.display_surface, "white", rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS["gray"], rect, 4, 4)

        # menu options
        for col in range(self.cols):
            for row in range(self.rows):
                x = rect.left + (rect.width / (self.cols * 2)) + (rect.width / self.cols) * col
                y = rect.top + (rect.height / (self.rows * 2)) + (rect.height / self.rows) * row
                i = col * 2 + row
                color = "black" if row == idx["row"] and col == idx["col"] else COLORS["gray"]

                text_surface = self.font.render(options[i], True, color)
                text_rect = text_surface.get_frect(center = (x, y))
                self.display_surface.blit(text_surface, text_rect)

    def switch(self):
        rect = pygame.FRect(self.left, self.top - 200, 400, 400)
        pygame.draw.rect(self.display_surface, "white", rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS["gray"], rect, 4, 4)

        # menu options
        for i in range(len(self.player_monsters)):
            x = rect.centerx 
            y = (
                rect.top + rect.height / (self.visible_monsters * 2) # get center of first division
                + (rect.height / self.visible_monsters * i) # add iteration of next division
            )

            name = self.player_monsters[i].name
            color = "black" if i == self.switch_idx else COLORS["gray"]
            text_surface = self.font.render(name, True, color)

            text_rect = text_surface.get_frect(center =  (x, y))
            if rect.collidepoint(text_rect.center):
                self.display_surface.blit(text_surface, text_rect)

    def update(self):
        self.input()

    def draw(self):
        match self.state:
            case "general": self.quad_select(self.general_idx, self.general_options)
            case "attack": self.quad_select(self.attack_idx, self.monster.abilities)
            case "switch": self.switch()
