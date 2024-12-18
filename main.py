from random import choice

from settings import *
from lib.helpers import *
from lib.monsters import Player, Opponent
from lib.ui import UI
from lib.timer import Timer

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Monster Battle')
        self.clock = pygame.time.Clock()
        self.running = True
        self.import_assets()

        # groups 
        self.all_sprites = pygame.sprite.Group()

        # data
        # player
        player_monster_list = [ "Sparchu", "Cleaf", "Jacana", "Gulfin", "Pouch", "Larvea"] # static data for testing
        self.player_monsters = [Player(x, self.back_surfaces[x]) for x in player_monster_list]
        self.monster = self.player_monsters[0]
        self.all_sprites.add(self.monster)

        # opponent
        opponent_name = choice(list(MONSTER_DATA.keys()))
        self.opponent = Opponent(opponent_name, self.front_surfaces[opponent_name], self.all_sprites)

        # ui
        self.ui = UI(self.monster, self.player_monsters, self.monster_icon_surfaces)

    def import_assets(self):
        self.back_surfaces = folder_importer("images", "back")
        self.front_surfaces = folder_importer("images", "front")
        self.bg_surfaces = folder_importer("images", "other")
        self.monster_icon_surfaces = folder_importer("images", "simple")

    def draw_floor(self):
        for sprite in self.all_sprites:
            floor_rect = self.bg_surfaces["floor"].get_frect(center = sprite.rect.midbottom + pygame.Vector2(0,-10))
            self.display_surface.blit(self.bg_surfaces["floor"], floor_rect)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
           
            # update
            self.all_sprites.update(dt)
            self.ui.update()

            # draw  
            self.display_surface.blit(self.bg_surfaces["bg"], (0,0))
            self.draw_floor()
            self.all_sprites.draw(self.display_surface)
            self.ui.draw()
            pygame.display.update()
        
        pygame.quit()
    
if __name__ == '__main__':
    game = Game()
    game.run()
