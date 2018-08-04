import pygame
from player import Player
from enemy_factory import EnemyFactory

# Constants
SCREEN_BACKGROUND_COLOR = (0,0,25)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

bullet_list = pygame.sprite.Group()

player = Player(SCREEN_WIDTH, bullet_list)
player.rect.x = SCREEN_WIDTH/2
player.rect.y = SCREEN_HEIGHT - 64

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

enemyFactory = EnemyFactory(SCREEN_WIDTH, all_sprites_list, bullet_list)

clock=pygame.time.Clock()

while not done:
   
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        # Check to see if we hit escape
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
                done = True

        # enmeyFactory update creates monsters
        enemyFactory.update()

        # Update the sprites and bullets
        all_sprites_list.update()
        bullet_list.update()

        # Check if a monster has been hit
        for entity in all_sprites_list:
                
                bullet_collide_list = pygame.sprite.spritecollide(entity, bullet_list, True)
                
                # Kill the entity if its hit a bullet
                if len(bullet_collide_list) > 0:
                        entity.kill()


        screen.fill(SCREEN_BACKGROUND_COLOR)

        # pygame.draw.rect(screen, (255,255,9), player.rect)
        # for b in bullets:
        #         pygame.draw.rect(screen, (0,255,9), b.rect)

        all_sprites_list.draw(screen)
        bullet_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

