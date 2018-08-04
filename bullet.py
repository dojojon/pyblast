import pygame

SPEED = -10

class Bullet(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, originX, originY):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Load the player image
        self.image = pygame.image.load('./assets/bullet.png').convert_alpha()
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        self.rect.x = originX - self.rect.width / 2
        self.rect.y = originY 

    def update(self):
        self.rect.y += SPEED
        if self.rect.y < 0:
            self.kill()
