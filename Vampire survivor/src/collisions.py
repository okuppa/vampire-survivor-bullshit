from settings import pygame

def player_collision_handler(player, *args):
    collisions = pygame.sprite.groupcollide(player.collidables, player.player_sprite, False, False)
    if collisions:
    
            dir = ''
            if args:
             for ar in args:
                if ar == 'horizontal' or ar == 'vertical':
                    dir = ar
        
            for sprite in collisions:
                if sprite.mask:
                    if sprite.type == 'projectile' and sprite.mask.overlap(player.mask, ((player.rect.x - sprite.rect.x),(player.rect.y - sprite.rect.y))):
                        print('overlap with projectile')
                    if sprite.type == 'block' and sprite.mask.overlap(player.mask, ((player.rect.x - sprite.rect.x),(player.rect.y - sprite.rect.y))):
                        print('block overlap')
                else:
                    pass

def player_block_collision_handler(player, dir, sprite):
    

    if dir == 'horizontal':
        if player.player_direction.x > 0: player.rect.right = sprite.rect.left
        else: player.rect.left = sprite.rect.right
    elif dir == 'vertical':
        if player.player_direction.y > 0: player.rect.bottom = sprite.rect.top
        else: player.rect.top = sprite.rect.bottom
        pass
    
