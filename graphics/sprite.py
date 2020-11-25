import pygame as pg

class Sprite():

    def render(self, screen, x=300, y=300):
        screen.blit(self.image, (x, y))

    '''if you want resize base on original width and height just pas a nem scaleFactor to be multiplied
      ,otherwise pass as parameter a new width and a new height
    '''
    def scale(self, scaleFactor=1, width=0, height=0):
        if(scaleFactor == 1):
            self.image = pg.transform.smoothscale(image, (width, height))
        else:
            newWidth = self.image.get_width() * scaleFactor
            newHeigth = self.image.get_height() * scaleFactor
            self.image = pg.transform.smoothscale(
                self.image, (newWidth, newHeigth))

    def __init__(self, image, scale=1):
        self.image = image
        self.mask = pg.mask.from_surface(image)
        self.originalImage = image
        if scale != 1:
            scale(self, scale)
            
    def rotate(self, degres):
        self.image = pg.transform.rotate(self.image, degres)

    def flip(self, xaxis = False , yaxis = False):
        self.image = pg.transform.flip(self.image, xaxis, yaxis)
        
    def restoreDefault(self):
        self.image = self.originalImage
        
    def get_width(self):
        return self.image.get_width()
    def get_height(self):
        return self.image.get_height()