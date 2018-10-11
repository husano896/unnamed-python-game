PYSDL2 = True
TestBench = False
Graphic_Thread = False

if (PYSDL2):
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
    import System.TextInput

if (TestBench):
    import Testbench

import os
import threading
#from _thread import *
#os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
os.environ['SDL_VIDEO_CENTERED'] = '1'

import pygame
from pygame.locals import *

from sys import exit
import System.Audio
import System.Item
from Scene.Copyright import Scene_Copyright
from Scene.__Changer__ import Scene_Changer
from Scene.Title import Scene_Title
from Scene.Battle import Scene_Battle
from Scene.Map import Scene_Map
######### INIT #########

FPS = 60 # frames per second, the general speed of the program

pygame.init()
print("Pygame Version " + pygame.version.ver)
print("SDL Version ", end='')
print(pygame.get_sdl_version())

####inject into pygame
class UPG():
    def __init__(self):
        global PYSDL2
        self.WINDOWWIDTH = 1280 # size of window's width in pixels
        self.WINDOWHEIGHT = 720 # size of windows' height in pixels
        self.BGCOLOR = (0, 0, 0)
        self.Version = "1.00 2018092x"
        self.Screen = pygame.display.set_mode((self.WINDOWWIDTH,self.WINDOWHEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
        
        self.Scene = None
        self.Network = None
        
        self.Audio = System.Audio
        self.Item = System.Item
        
        self.PySDL2 = PYSDL2

        self.DefaultFontSmall = pygame.font.Font("NotoSansCJKtc-Regular.otf", 8)
        self.DefaultFont = pygame.font.Font("NotoSansCJKtc-Regular.otf", 14)
        self.DefaultFontLarge = pygame.font.Font("NotoSansCJKtc-Regular.otf", 32)

        self.WindowSkin = pygame.image.load("Graphics/WindowSkins/Lang2fk.png").convert_alpha()
        self.events = []
        self.event = { 'MOUSEMOTION' : None,
                       'MOUSEBUTTONDOWN' : None,
                       'MOUSEBUTTONUP' : None

                    }
        self.chat_list = [ ("Test1", (255,255,255)),
                           ("Test2", (0,0,0)),
                           ("Test3", (255,0,0)),
                           ("Test4", (0,255,0)),
                           ("Test5", (0,0,255))
                           ]
        self.RenderEnabled = False
        
        if (PYSDL2):
            self.RenderEnabled = True
            self.TextInput = System.TextInput
            self.Renderer = pygame.render.Renderer(vsync=False)

    def ChangeScene(self, nextScene):
        
        print("change Scene: ", end='')
        print(nextScene)
        Scene_Changer(nextScene)
        
    def screenFill(self):
        if (self.RenderEnabled):
            self.Renderer.clear(self.BGCOLOR)
        else:
            self.Screen.fill(self.BGCOLOR)
        
pygame.UPG = UPG()
#Init Scene
pygame.UPG.ChangeScene(Scene_Map())
frame = 0
def EventsReset():
    pygame.UPG.event['MOUSEMOTION'] = None
    pygame.UPG.event['MOUSEBUTTONDOWN'] = None
    pygame.UPG.event['MOUSEBUTTONUP'] = None
                
def showFPS():
    global FPSCLOCK
    #img_FPS = pygame.UPG.DefaultFont.render("%.2f" % (FPSCLOCK.get_fps()) , 1, (127,127,127))
    #if (pygame.UPG.RenderEnabled):
    #    pygame.render.Sprite(pygame.UPG.Renderer.load_texture(img_FPS)).render((0,0))
    #else:
    #    pygame.UPG.Screen.blit(img_FPS,(0,0))
    pygame.display.set_caption("UPG %.2f" % (FPSCLOCK.get_fps()))
                               
def graphics_update():
    global FPSCLOCK2
    global frame
    FPSCLOCK2 = pygame.time.Clock()
    while True:
        try:
            #pygame.UPG.screenFill()
            if pygame.UPG.Scene != None:
                pygame.UPG.Scene.graphicsUpdate()
                
            if (pygame.UPG.RenderEnabled):
                pygame.UPG.Renderer.render_present()
            else:
                pygame.display.flip()

            frame +=1
            print(frame)

            FPSCLOCK2.tick(FPS)
        except Exception as e:
            raise(e)
        
        
        
def main():
    global FPSCLOCK, screen, Graphic_Thread
    FPSCLOCK = pygame.time.Clock()

    if Graphic_Thread:
        g_handler = threading.Thread(target=graphics_update)
        g_handler.start()
    
    while True:
        try:
            EventsReset()
            pygame.UPG.events = pygame.event.get()
            
            for event in pygame.UPG.events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == MOUSEMOTION:
                    cur_x, cur_y = event.pos
                    pygame.UPG.event['MOUSEMOTION'] = event
                elif event.type == MOUSEBUTTONDOWN:
                    cur_x, cur_y = event.pos
                    pygame.UPG.event['MOUSEBUTTONDOWN'] = event
                elif event.type == MOUSEBUTTONUP:
                    cur_x, cur_y = event.pos
                    pygame.UPG.event['MOUSEBUTTONUP'] = event

            if not Graphic_Thread:
                pygame.UPG.screenFill()
            
            if (pygame.UPG.Scene != None):
                pygame.UPG.Scene.update()
                
            #if (TestBench):
                #return Testbench.process()
                
            if not Graphic_Thread:
                pygame.UPG.Scene.graphicsUpdate()
                showFPS()
                if (pygame.UPG.RenderEnabled):
                    pygame.UPG.Renderer.render_present()
                else:
                    pygame.display.flip()

            FPSCLOCK.tick(FPS)
            
        except Exception as e:
            raise(e)
            if Graphic_Thread:
                g_handler.stop()
                
            
        
if __name__ == '__main__':
    main()
