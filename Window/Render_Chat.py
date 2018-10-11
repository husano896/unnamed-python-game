import pygame
from Window.RenderBase import Window_RenderBase

window_width, window_height = 400, 250
alpha = 127

class Window_Render_Chat(Window_RenderBase):
    
    def __init__(self, r = (window_width, window_height), Alpha = alpha):
        super(Window_Render_Chat, self).__init__(r = r, Alpha = Alpha)
        self.show_size = 12
        self.update_required = True

    def update(self):
        if (self.update_required):
            self.Image = self.BaseImage.copy()
            for i in range(min(self.show_size, len(pygame.UPG.chat_list))):
                self.Image.blit(self.font.render(pygame.UPG.chat_list[len(pygame.UPG.chat_list)-1-i][0], 1, pygame.UPG.chat_list[len(pygame.UPG.chat_list)-1-i][1]),
                                (8, self.BaseImage.get_height() - 20*(i+1)-5))
            self.update_required = False

            self.RenderRefresh()
            
    def add_text(self, x):
        pygame.UPG.chat_list.append((x,(255,255,255)))
        self.update_required = True
