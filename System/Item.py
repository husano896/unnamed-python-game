import pygame

#Items直接存Class

Items = []

def init():
    pass

class Item_Base:
    def __init__(self, name = "", rare = ""):
        self.Name = name
        self.Rare = rare
        self.ItemCount = 0
        self.Image = None
        self.RenderedImage = None
        
    #這函數應該要被複寫
    def UseItem(self):
        pass
        
init()
