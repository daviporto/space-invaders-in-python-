import pygame
from graphics import sprite


class SptriteSheet:
    def __init__(self, path):
        try:
            self.sheet = pygame.image.load(path)
        except pygame.error as msg:
            print("unable to load image at ", path)
            raise SystemExit("something wrong")

    def spriteAt(self, retctangle, invisibleColor=None):
        retctangle = pygame.Rect(retctangle)
        s = pygame.Surface(retctangle.size)
        s.blit(self.sheet, (0, 0), retctangle)
        if invisibleColor:
            s.set_colorkey(invisibleColor, pygame.RLEACCEL)

        return sprite.Sprite(s)

    def render(self, screen,  x=300, y=300):
        screen.blit(self.sheet, (x, y))

    def getSprites(self, Xamoutn=3, Yamount=4, width=0, height=0, invisibleColor=None):
        if not width:
            width = self.sheet.get_width() // Xamoutn
        if not height:
            height = self.sheet.get_height() // Yamount
            
        offsetX = offsetY = 0
        sprites = []
        for index in range(Xamoutn * Yamount):
            sprites.append(self.spriteAt(
                (offsetX * width, offsetY * height, width, height), invisibleColor))
            offsetX += 1
            if offsetX > Xamoutn:
                offsetX = 0
                offsetY += 1
            if offsetY > Yamount:
                offsetY = 0

        return sprites


if __name__ == "__main__":
    sh = aaaa("res/cracters/Female 09-1.png")
    sps = sh.getSprites()
