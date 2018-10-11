import pygame
from pygame.locals import *

class Sprite_Character(pygame.sprite.Sprite):
    def __init__(self, image = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.master_image = None
        self.rect = None
        self.topleft = 0,0
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1     
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.row = 0
        self.gravity = 0.0
        
    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename)#.convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = pygame.Rect(0,0,width,height)
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def freset(self):
        frame_x = (self.frame % self.columns) * self.frame_width
        frame_y = self.row * self.frame_height
        rect = ( frame_x, frame_y, self.frame_width, self.frame_height)
        self.image = self.master_image.subsurface(rect)
        self.old_frame = self.frame
            
    def update(self, current_time, rate=15):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = self.row * self.frame_height
            rect = ( frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame
