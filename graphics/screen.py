import pygame
from os import path
from graphics import colors

#
pygame.font.init()
defaultFont = font = pygame.font.SysFont("comicsansms", 35)

class progressBar():
    def __init__(self, x, y, width, height, percent, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.percent = percent
        self.color = color
        
    def update(self, percent):
        self.percent = percent
    
    def draw(self, canvas):
        currentWidth = self.width * self.percent // 100
        pygame.draw.rect(canvas, self.color, pygame.Rect(self.x, self.y, currentWidth, self.height))   
    
class Canvas:

    def __init__(self, width, height, title, background):
        self.canvas = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.background =  pygame.image.load(background)
        self.background = pygame.transform.smoothscale(
            self.background, (width, height))

    def redraw(self):
        self.canvas.blit(self.background, (0, 0))
        # self.canvas.blit(GreenSpaceShip, (200,200))

    def drawMob(self, mob):
        mob.draw(self.canvas)
        
    def drawImage(self, image, x =100, y = 100):
        self.canvas.blit(image, (x,y))

    def drawText(self, text, x,  y, color=colors.hexToRGB(0x999999), font=defaultFont, anchor='TL'):
        '''TL = top-left || TR = topRight || BL = bottomLeft || BR = bottnRight || C = center'''
        label = font.render(text, 1, color)

        if anchor == 'TL':
            pass
        elif anchor == 'C':
            x += (self.canvas.get_width() >> 1 )- (label.get_width() >> 1)
            y += (self.canvas.get_height() >> 1 )- (label.get_height() >> 1)
        elif anchor == 'TR':
            x += self.canvas.get_width() - label.get_width()
        elif anchor == 'BL':
            y += self.canvas.get_height() - label.get_height()
        else:
            x += self.canvas.get_width() - label.get_width()
            y += self.canvas.get_height() - label.get_height()

        self.canvas.blit(label, (x, y))
        

    def update(self):
        pygame.display.update()
