import pygame
import random


class entity():
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
    
    def collided(self, obj):
        offsetx = self.x + 60 - obj.x
        offsety = self.y - obj.y 
        return self.sprite.mask.overlap(obj.sprite.mask, (offsetx, offsety)) != None

        


class ship(entity):

    def __init__(self, x, y, sprite, laser,  helth=100, shootRate=45):
        entity.__init__(self, x, y, sprite)
        self.maxHelth = helth
        self.laser = laser
        self.shootRate = shootRate

    def draw(self, canvas):
        canvas.blit(self.sprite.image, (self.x, self.y))

    def update(self, movingX, direction, speed):
        if movingX % 2 == 0:
            if movingX < 100:
                self.x += int( direction * speed)
            else:
                self.y += 10 

    def getWidth(self):
        return self.sprite.get_width()

    def getHeight(self):
        return self.sprite.get_height()


class Projectile(entity):
    def __init__(self, x, y, sprite, speed = -10):
        entity.__init__(self,x, y, sprite)
        self.speed = speed

    def draw(self, canvas):
        canvas.blit(self.sprite.image, (self.x, self.y))

    def update(self):
        self.y += self.speed



class player(ship):
    def __init__(self, x, y, sprite, laser, health=100, lives = 3):
        ship.__init__(self, x, y, sprite, laser)
        self.shootcooldown = 0
        self.health = health
        self.lives = lives
        self.projectiles = []
        self.score = 0

    def shoot(self):
        if self.shootcooldown == 0:
            self.projectiles.append(Projectile(
                self.x + 20, self.y + 5, self.laser))
            self.shootcooldown = self.shootRate

    def update(self, height):
        if self.shootcooldown > 0:
            self.shootcooldown -= 1

        for projectile in self.projectiles:
            projectile.update()
            if projectile.y > height:
                projectiles.remove(projectile)


class ennemy(ship):
    bombs = []
    def __init__(self, enemySprite, laserSprite, x, y):
        ship.__init__(self,x, y, enemySprite, laserSprite)
        
    def bomb(self):
        ennemy.bombs.append(Projectile(self.x, self.y, self.laser, 10))

    def move(self, speed):
        self.y += speed
