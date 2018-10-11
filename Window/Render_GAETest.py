import pygame
from Window.RenderBase import Window_RenderBase
from pygame_button import pyButton
import json
import urllib2



window_width, window_height = 800, 550

class Window_Render_GAETest(Window_RenderBase):

    def __init__(self, r = (window_width, window_height)):
        super(Window_Render_GAETest, self).__init__(r, 8)
        self.Image = self.BaseImage.copy()

        current_x , current_y = (10, 10)
        
        self.buttonsGroup = pygame.sprite.Group()
        img1 = pygame.UPG.DefaultFontLarge.render("GAE Test", 1, (255,255,255))

        self.Image.blit(img1, (current_x, current_y))

        current_y += 10 + img1.get_height()
        
        self.start_x = current_x
        self.start_y = current_y
        self.BaseImage = self.Image.copy()

        super(Window_Render_GAETest, self).RenderRefresh()
        
    def update(self):
        if pygame.UPG.event['MOUSEBUTTONDOWN']:
            pos = pygame.UPG.event['MOUSEBUTTONDOWN'].pos
            if self.rect.collidepoint(pos):
                fetch_data()

    def fetch_data(self):
        #data should be a array here
        data = json.load(urllib2.urlopen('http://someurl/path/to/json'))
        self.Image = self.BaseImage.copy()

        print(data)

        current_x, current_y = self.start_x, self.start_y
        for i in data:
            #格式 { text : "文字", color : (255,255,255)}
            #JSON的Key這邊應該全部小寫
            img = pygame.UPG.DefaultFont.render(i.text, 1, i.color)
            self.Image.blit(img, (current_x, current_y))
            current_y += 5 + img.get_height()
            
        super(Window_Render_GAETest, self).RenderRefresh()
        
