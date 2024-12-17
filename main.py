from settings import *
from lib.helpers import *
from lib.monsters import Monster
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
        player_monster_list = [ "Sparchu", "Cleaf", "Jacana"] # static data for testing
        self.player_monsters = [Monster(x, self.back_surfaces[x]) for x in player_monster_list]
        self.monster = self.player_monsters[0]
        self.all_sprites.add(self.monster)

    def import_assets(self):
        self.back_surfaces = folder_importer("images", "back")
        self.bg_surfaces = folder_importer("images", "other")

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
           
            # update
            self.all_sprites.update(dt)

            # draw  
            self.display_surface.blit(self.bg_surfaces["bg"], (0,0))
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        
        pygame.quit()
    
if __name__ == '__main__':
    game = Game()
    game.run()
