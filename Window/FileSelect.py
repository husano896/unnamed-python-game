from Window.Base import Window_Base
import pygame
from pygame_button import pyButton

window_width, window_height = 800, 550

class Window_FileSelect(Window_Base):

    def __init__(self, r = (window_width, window_height)):
        super(Window_FileSelect, self).__init__(r, 8)
        self.image = self.BaseImage.copy()

        self.buttonsGroup = pygame.sprite.Group()
        img1 = pygame.UPG.DefaultFontLarge.render("FILE SELECT", 1, (255,255,255))

        self.image.blit(img1, (10, 10))
        for i in range(3):
            aa = pyButton(width = 760, height = 160)
            #這邊之後改成讀存檔
            img = pygame.UPG.DefaultFont.render(("FILE %d" % i), 1, (255,255,255))
            aa.image.blit(img, (20, 20))
            aa.rect.x = 20
            aa.rect.y = 40 + (160+10)*i
            self.buttonsGroup.add(aa)

        self.buttonsGroup.draw(self.image)
        self.BaseImage = self.image.copy()
        
    def update(self):
        #self.image = self.BaseImage.copy()
        #self.buttons.draw(self.image)
        if pygame.UPG.event['MOUSEBUTTONDOWN']:
            pos = pygame.UPG.event['MOUSEBUTTONDOWN'].pos
            #offset
            pos = (pos[0] - self.rect.x, pos[1] -self.rect.y)
            for i in self.buttonsGroup:
                if i.rect.collidepoint(pos):
                    print(i)
        pass
