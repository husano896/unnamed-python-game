import pygame

FontSize = (26,36)
init = False
DmgImage = None
MissImage = None
CriticalImage = None
DefaultFont = None

def Convert(damage = 0, critical = False, sp_damage = False):
    
    global init, DmgImage, MissImage, CriticalImage
    
    if (not init):
        DmgImage = pygame.image.load("Graphics/Strings/num.png").convert_alpha()
        MissImage = pygame.image.load("Graphics/Strings/miss.png").convert_alpha()
        CrititalImage = pygame.image.load("Graphics/Strings/critical.png").convert_alpha()
        DefaultFont = pygame.font.Font("NotoSansCJKtc-Black.otf", FontSize[0])

        init = True
        
    if (damage == "Miss"):
        return MissImage

    if (type(damage) == int):
        damage_int = damage
    
        damage_str = str(damage)
            
        damage_base_y = 0

        if (sp_damage):
            if (damage_int > 0):
                damage_base_y = 2
            else:
                damage_base_y = 4
        else:
            if (damage_int > 0):
                if (critical):
                    damage_base_y = 1
            else:
                damage_base_y = 3

        #準備圖像空間
        damage_img = pygame.Surface((FontSize[0]*len(damage_str), FontSize[1]), pygame.SRCALPHA)
        for i in range(len(damage_str)):
            Tnum_img = DmgImage.subsurface((FontSize[0] * int(damage_str[i]), FontSize[1]), FontSize)
            damage_img.blit(Tnum_img, (FontSize[0]*i, 0))

        if (critical):
            exdamage_img = pygame.Surface((FontSize[0]*len(damage_str), FontSize[1]+CrititalImage.get_height()), pygame.SRCALPHA)
            exdamage_img.blit(CrititalImage, ((FontSize[0]*len(damage_str) - CrititalImage.get_height())/2 , 0))
            exdamage_img.blit(CrititalImage, (0 , CrititalImage.get_height()))
            return exdamage_img
        return damage_img
    
    return DefaultFont.render(damage, 1, (255,255,255))
