import pygame
class pyButton(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color = (127,127,127), width = 1, height = 1):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height], pygame.SRCALPHA)
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

       #觸發事件
       def NoneEvent():
           pass
        
       self.event_LeftClick = NoneEvent
       self.event_RightClick = NoneEvent
       self.event_MoveIn = NoneEvent
       self.event_MoveOut = NoneEvent
       
    def setImage(self, img, reset = False):
        self.image = img
        if (reset == True):
            self.rect = self.image.get_rect()

    def HandleEvent(self, events):
        pass

    def update(self):
        pass
    
