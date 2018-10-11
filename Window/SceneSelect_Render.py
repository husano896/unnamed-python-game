#from Window.Base import Window_Base
from Window.RenderBase import Window_RenderBase
import pygame
from pygame_button import pyButton
from Scene.Battle import Scene_Battle
from Scene.Map import Scene_Map

window_width, window_height = 800, 550

class Window_SceneSelect(Window_RenderBase):

    def __init__(self, r = (window_width, window_height)):
        super(Window_SceneSelect, self).__init__(r, 8)
        self.image = self.BaseImage.copy()

        current_x , current_y = (10, 10)
        
        self.buttonsGroup = pygame.sprite.Group()
        img1 = pygame.UPG.DefaultFontLarge.render("Scene Select", 1, (255,255,255))

        self.image.blit(img1, (current_x, current_y))

        current_y += 10 + img1.get_height()
        
        img = pygame.UPG.DefaultFont.render("Scene_Battle", 1, (255,255,255))
        aa1 = pyButton(width = img.get_width() + 4, height = img.get_height() + 4)
        aa1.image.blit(img, (2, 2))
        aa1.rect.x = current_x
        aa1.rect.y = current_y
        
        current_y += 5 + img.get_height()

        img = pygame.UPG.DefaultFont.render("Scene_Map", 1, (255,255,255))
        aa2 = pyButton(width = img.get_width() + 4, height = img.get_height() + 4)
        aa2.image.blit(img, (2, 2))
        aa2.rect.x = current_x
        aa2.rect.y = current_y

        current_y += 5 + img.get_height()
        
        def aa1_Event():
            pygame.UPG.ChangeScene(Scene_Battle())

        def aa2_Event():
            pygame.UPG.ChangeScene(Scene_Map())
            
        aa1.event_LeftClick = aa1_Event

        aa2.event_LeftClick = aa2_Event
        self.buttonsGroup.add(aa1)
        self.buttonsGroup.add(aa2)
        
        self.buttonsGroup.draw(self.image)
        self.BaseImage = self.image.copy()

        super(Window_SceneSelect, self).RenderRefresh()
        
    def update(self):

        if pygame.UPG.event['MOUSEBUTTONDOWN']:
            pos = pygame.UPG.event['MOUSEBUTTONDOWN'].pos
            #offset
            pos = (pos[0] - self.rect.x, pos[1] -self.rect.y)
            for i in self.buttonsGroup:
                if i.rect.collidepoint(pos):
                    print(i)
                    i.event_LeftClick()
