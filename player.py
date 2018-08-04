import pygame
from bullet import Bullet

WHITE = (255, 255, 255)
SPEED = 4

class Player(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, screenWidth, bulletGroup):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.screenWidth = screenWidth

        # Load the player image
        self.image = pygame.image.load('./assets/scrap_ship.png').convert_alpha()
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        self.bulletGroup = bulletGroup


    def update(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moveLeft()
        elif keys[pygame.K_RIGHT]:
            self.moveRight()

        if keys[pygame.K_SPACE]:
            self.fire()

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > self.screenWidth - self.rect.width:
            self.rect.x = self.screenWidth - self.rect.width

    def moveLeft(self):
        self.rect.x -= SPEED

    def moveRight(self):
        self.rect.x += SPEED

    def fire(self):
        bullet = Bullet(self.rect.centerx, self.rect.y)
        self.bulletGroup.add(bullet)
