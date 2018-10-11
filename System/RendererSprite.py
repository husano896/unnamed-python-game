from pygame.render import *

class RendererSprite(pygame.render.Sprite):
    
    def __init__(self,img_tex = None, render = None):
        if (img_tex != None and render != None):
            self.setImage(img_tex, render)
        else:
            self.rect = (0,0)
            self.image = None
            self.renderedImage = None
        
    def setImage(self, image, renderer):
        self.rect = image.get_rect()
        self.image = image
        self.renderedImage = renderer.load_texture(image)
        
        pygame.render.Sprite.__init__(self, self.renderedImage)
        
    def collidePoint(self,point)
        return self.rect.collidepoint(point)

    def draw(self):
        if (self.renderedImage):
            self.renderedImage.render((self.rect.x, self.rect.y))
