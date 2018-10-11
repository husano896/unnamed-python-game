import pygame

pygame.init()

class pygame_Button(pygame.sprite.Sprite):

    color_bg = (127, 127, 127)
    color_border = (0, 0, 0)
    border = 2

    def __init__(self, size = None, text = "", event = None, style = 1):
        
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        myfont = pygame.font.Font("NotoSansCJKtc-Black.otf", 16)
        text_img = myfont.render(text, 1, (0,0,0))

        if (size == None):
            self.image = pygame.Surface((text_img.get_width() + self.border * 2, text_img.get_height() + self.border * 2), pygame.SRCALPHA)
        else:
            self.image = pygame.Surface(size,pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.text = text
        self.command = event
        if (style == 0):
            self.image.fill(self.color_bg)
            #pygame.draw.rect(self.image, self.color_border, self.rect, self.border)
        elif (style == 1):
            pygame.draw.ellipse(self.image, self.color_bg, self.rect, 0)
            #pygame.draw.ellipse(self.image, self.color_border, self.rect, self.border)
        
        self.image.blit(text_img,
                        (self.image.get_width()/2 - text_img.get_width()/2,
                         self.image.get_height()/2 - text_img.get_height()/2))

    def update(self, ev):
        action = ev['mouse_button']
        mouse_rect = ev['mouse_axis']
        if (action[0] == True):
            if (not self.command == None):
                if (self.rect.collidepoint(mouse_rect) == True):
                    self.command()
