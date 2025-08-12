from settings import *
from sprites import *

class ClassPlayer(pygame.sprite.Sprite):
    
    def __init__(self, playersprite, allsprites, collgroup):

        super().__init__(playersprite, allsprites)
        self.image = pygame.image.load(join('images', 'player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.speed = 500
        self.mask = pygame.mask.from_surface(self.image)

        self.player_direction = pygame.math.Vector2()
        self.direction_vector = math.Vector2()
        self.type = 'player'
        
        self.cscc_cooldown = 500
        self.ball_cooldown = 500

        self.last_cscc_shot = 0
        self.last_ball_shot = 0

        self.player_sprite = playersprite
        self.all_sprites = allsprites
        self.collidables = collgroup
        
        self.radius_around_player = 150
        self.aim_ball = AimTest(self.all_sprites)
    

    def movement(self, player_direction, dt):
        
        self.player_direction = player_direction.normalize() if player_direction else player_direction

        self.rect.x += player_direction.x * self.speed * dt
        direction = 'horizontal'
        self.player_collisions(direction)
        self.rect.y += player_direction.y * self.speed * dt
        direction = 'vertical'
        self.player_collisions(direction)
 

    def update(self, dt):
        
        self.aim_location()
        self.inputs(dt)
        self.player_collisions()
    
    def inputs(self, dt):
        
        keys = pygame.key.get_pressed() #get game keys on running

        player_direction = pygame.math.Vector2((keys[pygame.K_d] - keys[pygame.K_a]),keys[pygame.K_s] - keys[pygame.K_w])
        if player_direction.length_squared() > 0: 
           self.movement(player_direction, dt)

        if keys[pygame.K_b] and (pygame.time.get_ticks() >= (self.last_cscc_shot + self.cscc_cooldown)):
            self.last_cscc_shot = pygame.time.get_ticks()
            self.create_block()

        if keys[pygame.K_g] and (pygame.time.get_ticks() >= (self.last_ball_shot + self.ball_cooldown)):
            self.last_ball_shot = pygame.time.get_ticks()
            self.shoot_ball()
           
    def create_block(self):
        CollisionSprite((random.randint(50, WINDOW_WIDTH), random.randint(50, WINDOW_HEIGHT)), ((random.randint(20,60), random.randint(30,90))), self.collidables, self.all_sprites)

    def aim_location(self):
        mouse = math.Vector2(pygame.mouse.get_pos())

        self.direction_vector.x = mouse.x - self.rect.centerx
        self.direction_vector.y = mouse.y - self.rect.centery
        
        
        self.aim_ball.rect.center = mouse
   
        if self.direction_vector.x > self.radius_around_player:
            self.aim_ball.rect.centerx = self.rect.centerx + self.radius_around_player 
        elif self.direction_vector.x < -self.radius_around_player:
            self.aim_ball.rect.centerx = self.rect.centerx - self.radius_around_player
        
        if self.direction_vector.y > self.radius_around_player:
            self.aim_ball.rect.centery = self.rect.centery + self.radius_around_player
        elif self.direction_vector.y < -self.radius_around_player:
            self.aim_ball.rect.centery = self.rect.centery - self.radius_around_player

    def shoot_ball(self):
        print(self.direction_vector)
        direction = pygame.Vector2(self.direction_vector)
        BallSprite(self.aim_ball.rect.center, self.collidables, self.all_sprites, direction)

    def player_collisions(self, *args):
        player_collision_handler(self, *args)