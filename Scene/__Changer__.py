import pygame
from Scene.__Base__ import __Base__
class Scene_Changer(__Base__):

    def __init__(self, newscene, speed = 8):
        self.frame = 0
        self.speed = speed
        self.Img_LastScene = pygame.UPG.Screen.copy()
        
        newscene.update()
        self.Img_NewScene = pygame.UPG.Screen.copy()
        
        self.new_scene = newscene

        self.new_scene.onChange()
        
        pygame.UPG.Scene = self
        
    def update(self):
        
        self.Img_NewScene.set_alpha(self.frame)

        pygame.UPG.Screen.blit(self.Img_LastScene, (0,0))
        pygame.UPG.Screen.blit(self.Img_NewScene, (0,0))
        self.frame+=self.speed
        
        if (self.frame >= 256):
            self.new_scene.onChangeDone()
            pygame.UPG.Scene = self.new_scene
