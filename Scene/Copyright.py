import pygame, math
from Scene.__Base__ import __Base__
from Scene.__Changer__ import Scene_Changer
from Scene.Title import Scene_Title

class Scene_Copyright(__Base__):
    def __init__(self):
        self.SE = pygame.UPG.Audio.Sound("cgefc30.wav")
        self.image = pygame.Surface((800,600))

        #text_0 = pygame.UPG.DefaultFontLarge.render("NOTICE", 1, (200,0,0))
        text_1 = pygame.UPG.DefaultFontLarge.render("本遊戲所使用之部分素材為第三方所有", 1, (255,255,255))
        text_2 = pygame.UPG.DefaultFontLarge.render("僅供學術性研究　無意侵犯著作權", 1, (255,255,255))
        #self.image.blit(text_0, (400-text_0.get_width()/2,0))
        self.image.blit(text_1, (400-text_1.get_width()/2,96))
        self.image.blit(text_2, (400-text_2.get_width()/2,144))
        
        self.frame = 0
        
    def onChange(self):
        self.SE.play()
 
    def update(self):
        self.frame += 1
        self.image.set_alpha(int(255 * math.sin(math.radians(self.frame))))
        pygame.UPG.Screen.blit(self.image,(0,0))

        if (self.frame >= 180):
            Scene_Changer(Scene_Title())
