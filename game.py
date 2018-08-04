import pygame
from player import Player

# Consts
SCREEN_BACKGROUND_COLOR = (0,0,25)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

player = Player(SCREEN_WIDTH)
player.rect.x = 30
player.rect.y = 30

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

        screen.fill(SCREEN_BACKGROUND_COLOR)

        all_sprites_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

