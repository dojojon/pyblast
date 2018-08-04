import pygame
from player import Player

# Consts
SCREEN_BACKGROUND_COLOR = (0,0,25)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

bullets = pygame.sprite.Group()

player = Player(SCREEN_WIDTH, bullets)
player.rect.x = SCREEN_WIDTH/2
player.rect.y = SCREEN_HEIGHT - 64

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)


clock=pygame.time.Clock()

while not done:
   
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
                done = True

        all_sprites_list.update()
        bullets.update()

        screen.fill(SCREEN_BACKGROUND_COLOR)

        # pygame.draw.rect(screen, (255,255,9), player.rect)
        # for b in bullets:
        #         pygame.draw.rect(screen, (0,255,9), b.rect)

        all_sprites_list.draw(screen)
        bullets.draw(screen)


        pygame.display.flip()

        clock.tick(60)

