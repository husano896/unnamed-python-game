import pygame
from Scene.__Base__ import __Base__
from Window.FileSelect import Window_FileSelect
from Window.SceneSelect import Window_SceneSelect
class Scene_Title(__Base__):
    def __init__(self):
        self.AAA = 1
        self.BGM = "BD_211.ogg"
        self.frame = 254
        self.Clicked = False
        
        #self.Window = Window_FileSelect()
        self.Window = Window_SceneSelect()
        self.Window.rect.x = 240
        self.Window.rect.y = 85
        self.WindowGroup = pygame.sprite.Group(self.Window)
        
    def onChange(self):
        pygame.UPG.Audio.playBGM(self.BGM)
        
    def update(self):

        if (self.Clicked):
            bgcolor = max(255-self.frame, 192)
            pygame.UPG.Screen.fill((bgcolor, bgcolor, bgcolor))

            if (self.frame < 64):
                self.frame += 3
                return
            
            #窗口更新
            self.Window.update()
            #畫面描繪
            self.WindowGroup.draw(pygame.UPG.Screen)
            
        else:
            self.frame += 2
            bgcolor = min(self.frame, 255)
            pygame.UPG.Screen.fill((bgcolor, bgcolor, bgcolor))

            if (self.frame < 256):
                return

            #接收按鍵輸入
            if (pygame.UPG.event['MOUSEBUTTONDOWN']):
                self.Clicked = True
                self.frame = 0
                
            a_op = (self.frame%170)
            if (a_op > 85):
                a_op = 170 - a_op

            img = pygame.UPG.DefaultFontLarge.render("TAP TO START", 1, (a_op*3,a_op*3,a_op*3))
            pygame.UPG.Screen.blit(img,(pygame.UPG.WINDOWWIDTH/2-img.get_width()/2,pygame.UPG.WINDOWHEIGHT*2/3))
        
        
        img2 = pygame.UPG.DefaultFont.render(pygame.UPG.Version, 1, (127,127,127))
        pygame.UPG.Screen.blit(img2,(0,pygame.UPG.WINDOWHEIGHT-img2.get_height()))
