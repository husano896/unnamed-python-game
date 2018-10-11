from pygame.render import *

class RendererSpriteGroup:
    
    def __init__(self):

        self.sprites = []

    def add(self, spr)
        self.sprites.append(spr)

    def collideSprite(self, spr)
        return self.collides(spr)
    
    def collidePointAny(self,point)
        s = []
        for i in self.sprites:
            if (i.rect.collidepoint(point))
                s.append(i)

        return s

    def draw(self):
        for i in self.sprites:
            i.render((i.rect.x, i.rect.y))
