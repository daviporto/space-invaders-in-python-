import pygame
import os
import graphics.screen as screen
import graphics.spriteSheet as spriteSheet
from graphics.colors import red
import mob.entities as entities
import random
from util.math import clamp
from graphics.colors import black

pygame.font.init()
WIDTH = 900
HEIGHT = WIDTH * 9 // 16 + 100
TITLE = "Space Invaders"

shipsSheet = spriteSheet.SptriteSheet(os.path.join('res', 'ships.png'))
lasersSheet = spriteSheet.SptriteSheet(os.path.join('res', 'lasers.png'))
enemiesSheet = spriteSheet.SptriteSheet(os.path.join('res', 'enemies.png'))
background = os.path.join('res', 'background.png')
heart = pygame.image.load(os.path.join('res', 'heart.png'))

shipsSprites = shipsSheet.getSprites(4, 1, invisibleColor=black)
laserSprites = lasersSheet.getSprites(6, 1)
enemiesSprites = enemiesSheet.getSprites(4, 1, 66, 50, invisibleColor=black)

canvas = screen.Canvas(WIDTH, HEIGHT, TITLE, background)
font = pygame.font.SysFont("comicsansms", 72)
canvas.drawImage(shipsSheet.sheet)
running = True
FPS = 60
level = 1
playerSpeed = 5
waveLen = 5
ennemy_mov_speed = 1
clock = pygame.time.Clock()

player = entities.player(
    WIDTH // 2 - 50, HEIGHT - 100, shipsSprites[2], laserSprites[4])

heath_bar = screen.progressBar(
    WIDTH // 2 - 100, HEIGHT - 25, 150, 15, 100, red)
enemies = []
for i in range(1):
    enemies.append(entities.ennemy(
        enemiesSprites[0], laserSprites[0], 50 + enemiesSprites[0].get_width() * i * 2, 20))


def Keyboard(keys):
    WidthMax = WIDTH - player.getWidth()
    HeightMax = HEIGHT - player.getHeight()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x = clamp(player.x - playerSpeed, 0,  WidthMax)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x = clamp(player.x + playerSpeed, 0, WidthMax)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y = clamp(player.y + playerSpeed, 0, HeightMax)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y = clamp(player.y - playerSpeed, 0, HeightMax)
    if keys[pygame.K_SPACE]:
        player.shoot()

movingX, diretction, time = 0, 1, 0
while(running):
    #code that runs if player lost or not 
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if player.lives == 0 or player.health <= 0:
        #runs just in lost screen
        canvas.drawText("you lost", 0, 0, anchor='C')
        canvas.drawText(f"your score is {player.score}", 0, 50, anchor='C')
        canvas.drawText("press enter to play again", 0, 100, anchor='C')
        
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            level = 1
            waveLen = 5
            player.health = 100
            player.lives = 3

    else:
        canvas.redraw()
        canvas.drawText(f"level {level}", 2, 2)
        for i in range(player.lives):
            canvas.drawImage(heart, 730 + (i * 50 + 20), 20)
    
        canvas.drawText('heath:', WIDTH // 2 - 180, -7, anchor='BL')
        heath_bar.update(player.health)
        heath_bar.draw(canvas.canvas)

        canvas.drawMob(player)
        for enemy in enemies:
            canvas.drawMob(enemy)
            enemy.update(movingX, diretction, ennemy_mov_speed)
            if enemy.y >= HEIGHT:
                player.lives -= 1
                enemies.remove(enemy)
                score += 1

        for bomb in entities.ennemy.bombs:
            bomb.update()
            canvas.drawMob(bomb)
            if player.collided(bomb):
                entities.ennemy.bombs.remove(bomb)
                player.health -= 10

        movingX += 1

        if movingX > 100:
            movingX = 0
            diretction *= -1

        for projectile in player.projectiles:
            canvas.drawMob(projectile)

        canvas.update()
        player.update(HEIGHT)

        if not enemies:
            level += 1
            waveLen += 5
            if waveLen >= 40:
                ennemy_mov_speed += 0.2
            if waveLen <= 40:
                colum = -1
                for i in range(waveLen):
                    if i % 10 == 0:
                        colum += 1
                    enemies.append(entities.ennemy(
                        enemiesSprites[colum], laserSprites[colum], 67 * (i % 10) + 110, colum * 55 + 30))

        for projectile in player.projectiles:
            for enemie in enemies:
                if enemie.collided(projectile):
                    enemies.remove(enemie)
                    player.projectiles.remove(projectile)

        time += 1
        if time % FPS - waveLen == 0:
            if len(enemies) > 0:
                enemies[random.randint(0, len(enemies) - 1)].bomb()
        Keyboard(pygame.key.get_pressed())


