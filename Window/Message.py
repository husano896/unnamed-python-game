import pygame
from Window_Base import Window_Base
from Game_System  import Game_System 
window_width, window_height = 960, 480
    
class Window_Message(Window_Base):

    def __init__(self, text):
        super(Window_Message, self).__init__((window_width, window_height))
        myfont = pygame.font.Font("Data\\msjh.ttf", 24)
        myfont2 = pygame.font.Font("Data\\msjh.ttf", 16)
        self.image = self.BaseImage.copy()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 160, 120
        self.text = text
        texts = text.split("\n")
        for i in range(len(texts)):
            if (texts[i] == ""):
                continue
            img_text = myfont.render(texts[i], 1, (255,255,255))
            self.image.blit(img_text, (self.Border, self.Border + i*28))

        img_text = myfont2.render("用力的按左鍵繼續 >>", 1, (255,255,255))
        self.image.blit(img_text, (self.rect.width - self.Border - img_text.get_width(), self.rect.height - self.Border - 20))        
        Game_System.Event_Handler.Event_Pause = True
        Game_System.SpriteGroupTop.add(self)
        
    def update(self):
        
        if (Game_System.mouse_button_trigger[0]):
            self.kill()
            Game_System.Event_Handler.Continue_Event()
            return
