import pygame
from Window_Base import Window_Base
from Game_System  import Game_System
from pygame_Button import pygame_Button
window_width, window_height = 500, 48
    
class Window_MenuBar(Window_Base):

    def __init__(self, r = (window_width, window_height)):
        super(Window_MenuBar, self).__init__(r)
        self.myfont = pygame.font.Font("Data\\msjh.ttf", 18)
        self.image = self.BaseImage.copy()
        self.rect = self.image.get_rect()
        self.show_size = 10
        self.chat_list = []
        self.update_required = True
        self.SpriteGroup = pygame.sprite.Group()
    
        self.button1 = pygame_Button(text = "系統", size = (80,22),event = lambda:(self.button1.image.set_shifts((0,0,127,63))))
        self.button2 = pygame_Button(text = "狀態", size = (80,22), event = lambda:(self.button2.image.set_shifts((0,0,127,63))))
        self.button3 = pygame_Button(text = "物品", size = (80,22), event = lambda:(self.button3.image.set_shifts((0,0,127,63))))
        self.button4 = pygame_Button(text = "技能", size = (80,22), event = lambda:(self.button4.image.set_shifts((0,0,127,63))))
        

        self.button1.rect.x, self.button1.rect.y = 3,3
        self.button2.rect.x, self.button2.rect.y = 86, 3
        self.button3.rect.x, self.button3.rect.y = 169, 3
        self.button4.rect.x, self.button4.rect.y = 252, 3
        self.SpriteGroup.add(self.button1)
        self.SpriteGroup.add(self.button2)
        self.SpriteGroup.add(self.button3)
        self.SpriteGroup.add(self.button4)
    def update(self):
        if (self.update_required):
            self.image = self.BaseImage.copy()

        ev = {'mouse_button': Game_System.mouse_button_trigger,
              'mouse_axis' : (Game_System.mouse_x - self.rect.x, Game_System.mouse_y - self.rect.y)}
        self.SpriteGroup.update(ev)
        self.SpriteGroup.draw(self.image)
        
Game_System.Window_MenuBar = Window_MenuBar()
