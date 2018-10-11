from Window.Base import Window_Base
import pygame
window_width, window_height = 400, 170
    
class Window_BattleChar(Window_Base):

    def __init__(self, actor = None):
        super(Window_BattleChar, self).__init__((window_width, window_height))
        self.Char = actor

        #Player Head
        pygame.draw.rect(self.image, (127,127,127), pygame.Rect((10,10), (150,150)) )
        #PlayerName
        img_name = pygame.UPG.DefaultFontLarge.render("PLAYER", 1, (255,255,255))
        self.image.blit(img_name, (170, 10))
        #HP Inside
        HP_PointList = [ (0 + 170,0 + 90), (200 + 170,0 + 90), (180 + 170,20 + 90), (0 + 170, 20 + 90)]
        pygame.draw.polygon(self.image, (255,255,255), HP_PointList)
        #SP Inside
        SP_PointList = [ (0 + 170,40 + 90), (170 + 170,40 + 90), (150 + 170,60 + 90), (0 + 170, 60 + 90)]
        pygame.draw.polygon(self.image, (255,255,255), SP_PointList)
        
        #self.image = self.BaseImage.copy()
        self.update_required = False

    def update(self):
        if (self.update_required):
            self.image = self.BaseImage.copy()
