from src.settings import *
from player import ClassPlayer

class Game():

 
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #create display surface
        pygame.display.set_caption("Vampire Survivor")
        
        self.clock = pygame.time.Clock()

        #groups
        self.player_sprites = pygame.sprite.Group()
        self.collidables = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        #create player
        self.player = ClassPlayer(self.player_sprites, self.all_sprites, self.collidables)
        self.running = True

    def run(self):
        
    
        
        while self.running == True: 

            dt = self.clock.tick()/1000
            

            self.display_surface.fill("#50297c") 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            

            self.all_sprites.draw(self.display_surface)
            self.all_sprites.update(dt)
            self.collidables.draw(self.display_surface)
            self.collidables.update(dt)

            pygame.display.update()


if __name__ == "__main__": #if its ran from __main__

    game = Game()
    game.run()