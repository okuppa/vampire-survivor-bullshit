from settings import *

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups, allsprites):
        super().__init__(groups, allsprites)
        self.image = pygame.Surface(size)
        self.image.fill(generate_random_color())

        self.rect = self.image.get_frect(center=pos)

        self.type = 'block'

        self.mask = pygame.mask.from_surface(self.image)

class AimTest(pygame.sprite.Sprite):
    def __init__(self, allsprites):

        super().__init__(allsprites)
        self.image = pygame.Surface((15,15))
        self.image.fill(generate_random_color())
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))


class BallSprite(pygame.sprite.Sprite):
    def __init__(self, pos, groups, allsprites, direction):
        super().__init__(groups, allsprites)
        self.image = pygame.Surface((50,50), pygame.SRCALPHA) # creates a surface, pygame.srcalpha makes the created surface transparent
   
        self.rect = self.image.get_frect(center=pos)
        self.drawn_circle = pygame.draw.circle(self.image, generate_random_color(), (15, 15), 10) #the center point of the drawn circle is not relative to the screen, but to the surface it is drawn on (fun)
        self.type = 'player_projectile'

        self.speed = 500

        self.direction = direction
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self, dt):
        
        self.rect.center += self.direction.normalize() * self.speed * dt 