import pygame

class Window_Base(pygame.sprite.Sprite):
    
    Border = 3
    alpha = 224
    BG_Color = (0,0,192,127)
    FG_Color = (127,127,127)
    
    def __init__(self, r = (1,1), border = Border, Alpha = alpha):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(r, pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        
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
        self.image.blit(bg_scaled, (0,0))
        #ULine
        self.image.blit(skin_U_Line, (16,0))
        #DLine
        self.image.blit(skin_D_Line, (16,r[1]-16))
        #LLine
        self.image.blit(skin_L_Line, (0,16))
        #RLiNE
        self.image.blit(skin_R_Line, (r[0]-16, 16))
        
        #LU Corner
        self.image.blit(skin_LU_Corner, (0, 0))
        #LD Corner
        self.image.blit(skin_LD_Corner, (0, r[1]-16))
        #RU Corner
        self.image.blit(skin_RU_Corner, (r[0]-16, 0))
        #RD Corner
        self.image.blit(skin_RD_Corner, (r[0]-16, r[1]-16))
        
        self.BaseImage = self.image.copy()
        
    def update(self):
        pass
