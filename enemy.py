import pygame
from bullet import Bullet

WHITE = (255, 255, 255)
SPEED = 4

class Enemy(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, screenWidth, screenHeight, bulletGroup, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        # Load the player image
        self.image = pygame.image.load('./assets/monster_1.png').convert_alpha()
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.bulletGroup = bulletGroup

    def update(self):
       self.rect.y +=1
       if self.rect.y > self.screenHeight:
           self.kill()

    def fire(self):
        bullet = Bullet(self.rect.centerx, self.rect.y)
        self.bulletGroup.add(bullet)
