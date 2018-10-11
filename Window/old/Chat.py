from Window.Base import Window_Base
import pygame
window_width, window_height = 400, 250
    
class Window_Chat(Window_Base):

    def __init__(self, r = (window_width, window_height)):
        super(Window_Chat, self).__init__(r)
        self.image = self.BaseImage.copy()
        self.show_size = 12
        self.chat_list = [("Test1", (255,255,255)), ("Test2", (0,0,0)), ("Test3", (255,0,0)), ("Test4", (0,255,0)), ("Test5", (0,0,255)) ]
        self.update_required = True

    def update(self):
        if (self.update_required):
            self.image = self.BaseImage.copy()
            for i in range(min(self.show_size, len(self.chat_list))):
                self.image.blit(self.font.render(self.chat_list[len(self.chat_list)-1-i][0], 1, self.chat_list[len(self.chat_list)-1-i][1]), (5, self.BaseImage.get_height() - 20*(i+1)-5))
            self.update_required = False
            
    def add_text(self, x):
        self.chat_list.append((x,(255,255,255)))
        self.update_required = True
