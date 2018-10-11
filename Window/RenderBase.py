import pygame
from pygame.render import *

class Window_RenderBase(pygame.render.Sprite):

    alpha = 224
    Border = 3
    
    def __init__(self,r = (1,1), border = Border, Alpha = alpha):
        
        image = pygame.Surface(r, pygame.SRCALPHA)
        self.rect = image.get_rect()

        self.font = pygame.font.Font("NotoSansCJKtc-Black.otf", 18)

        skin_bg = pygame.UPG.WindowSkin.subsurface((0,0,128,128)).convert()

        skin_LU_Corner = pygame.UPG.WindowSkin.subsurface((128,0,16,16))
        skin_LD_Corner = pygame.UPG.WindowSkin.subsurface((128,64-16,16,16))
        skin_RU_Corner = pygame.UPG.WindowSkin.subsurface((192-16,0,16,16))
        skin_RD_Corner = pygame.UPG.WindowSkin.subsurface((192-16,64-16,16,16))

        skin_U_Line = pygame.UPG.WindowSkin.subsurface((128+16,0,32,16))
        skin_D_Line = pygame.UPG.WindowSkin.subsurface((128+16,64-16,32,16))
        skin_L_Line = pygame.UPG.WindowSkin.subsurface((128,16,16,32))
        skin_R_Line = pygame.UPG.WindowSkin.subsurface((192-16,16,16,32))

        skin_U_Line = pygame.transform.scale(skin_U_Line, (r[0]-32, 16))
        skin_D_Line = pygame.transform.scale(skin_D_Line, (r[0]-32, 16))
        skin_L_Line = pygame.transform.scale(skin_L_Line, (16, r[1]-32))
        skin_R_Line = pygame.transform.scale(skin_R_Line, (16, r[1]-32))
        
        bg_scaled = pygame.transform.scale(skin_bg, r)
        bg_scaled.set_alpha(Alpha)

        #BG
        image.blit(bg_scaled, (0,0))
        #ULine
        image.blit(skin_U_Line, (16,0))
        #DLine
        image.blit(skin_D_Line, (16,r[1]-16))
        #LLine
        image.blit(skin_L_Line, (0,16))
        #RLiNE
        image.blit(skin_R_Line, (r[0]-16, 16))
        
        #LU Corner
        image.blit(skin_LU_Corner, (0, 0))
        #LD Corner
        image.blit(skin_LD_Corner, (0, r[1]-16))
        #RU Corner
        image.blit(skin_RU_Corner, (r[0]-16, 0))
        #RD Corner
        image.blit(skin_RD_Corner, (r[0]-16, r[1]-16))

        self.BaseImage = image.copy()
        self.Image = image.copy()
        self.RenderedImage = pygame.UPG.Renderer.load_texture(self.BaseImage)
        
        pygame.render.Sprite.__init__(self, self.RenderedImage)

    def RenderRefresh(self):
        self.RenderedImage = pygame.UPG.Renderer.load_texture(self.Image)
        
        pygame.render.Sprite.__init__(self, self.RenderedImage)
        
    #相容
    def draw(self):
        self.pos = (self.rect.x, self.rect.y)
        self.render()
        
    def update(self):
        pass
