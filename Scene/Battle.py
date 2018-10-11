import pygame
from Scene.__Base__ import __Base__

from Window.BattleChar import Window_BattleChar

class Scene_Battle(__Base__):
    
    def __init__(self, BGM = "cgbgm_b0.wav", Background = "CG0018993.bmp"):
        self.BGM = BGM
        self.frame = 0
        self.Background = pygame.image.load("Graphics/BattleBG/%s" % Background).convert()
        self.Background = pygame.transform.smoothscale(self.Background, (1280,960))
        self.Background.set_colorkey((0,0,0))
        self.BattleStart = False

        self.SpriteGroup = pygame.sprite.Group()
        self.Window_BTChar = Window_BattleChar()
        self.Window_BTChar.rect.x, self.Window_BTChar.rect.y = 0, 550
        self.SpriteGroup.add(self.Window_BTChar)

        if (pygame.UPG.PySDL2):
            pygame.UPG.TextInput.TextBoxLocation = (0, 528)
            
    def onChange(self):
        pass
    
    def onChangeDone(self):
        pygame.UPG.Audio.playBGM(self.BGM)
        self.BattleStart = True
        
    def update(self):
        if self.BattleStart:
            pygame.UPG.Screen.blit(self.Background, (0,-120))
            self.SpriteGroup.draw(pygame.UPG.Screen)
        else:
            pygame.UPG.Screen.fill((0,0,0))

        if (pygame.UPG.PySDL2):
            pygame.UPG.TextInput.update()
