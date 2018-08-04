import pygame
import random
from enemy import Enemy

class EnemyFactory():

    def __init__(self, screenWidth, screenHeight, allGroup, bulletGroup):

        self.bulletGroup = bulletGroup
        self.allGroup = allGroup
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    def update(self):
        print('Update enemy factory')

        enemyCount = len(self.allGroup) - 1

        if(enemyCount < 2):
            self.makeEnemy()

    def makeEnemy(self):
        x = random.randint(0, self.screenWidth)
        y = random.randint(0, 20)
        enemy = Enemy(self.screenWidth, self.screenHeight, self.bulletGroup, x , y)
        self.allGroup.add(enemy)