import pygame
from pygame.locals import *
from Scene.__Base__ import __Base__
from SpriteR.Character import SpriteR_Character
from Window.Render_Chat import Window_Render_Chat
import Map_Render

try:
    from pygame.render import *
except:
    pass

class Scene_Map(__Base__):
    audio_bgm_filename = "Audio/BGM/credits.ogg"
    frame = 0

    def __init__(self):

        self.map_1 = Map_Render.load_map('Maps//testmap.map')
        self.map_img = Map_Render.render_map(self.map_1)
        self.map_imgRendered = [
            pygame.render.Sprite(pygame.UPG.Renderer.load_texture(self.map_img[0])),
            pygame.render.Sprite(pygame.UPG.Renderer.load_texture(self.map_img[1])),
            pygame.render.Sprite(pygame.UPG.Renderer.load_texture(self.map_img[2]))
        ]


        self.camera_x = 0
        self.camera_y = 0
       # self.background = pygame.transform.scale(pygame.image.load("Graphics\\927950_20070628_screen029.jpg").convert(), (800,600))
        
        #b = pygame.transform.scale(pygame.image.load("Graphics\\BattleBG\\CG1007068.bmp").convert(), (800,600))
       # b.set_colorkey((0,0,0))
       # self.background.blit(b, (0,0))
        
        self.character = SpriteR_Character()
        self.character.load("Data\\0.png",32,48,4)

        #self.Battler = Game_Battler()

        #self.Window_BC = Window_BattleChar(char = self.Battler)
        self.Render_Chat = Window_Render_Chat()
        self.Render_Chat.rect.x, self.Render_Chat.rect.y = 0, 510

        #self.SpriteGroup = pygame.sprite.Group()
        #self.SpriteGroup.add(self.character)
        
        self.LastButtons = pygame.key.get_pressed()

        self.text = pygame.UPG.DefaultFont.render("%d,%d" % (self.camera_x, self.camera_y), 1, (255,255,255))
        self.text2 = pygame.UPG.DefaultFont.render(self.map_1['name'], 1, (255,255,255))

        if (pygame.UPG.PySDL2):
            pygame.UPG.RenderEnabled = True

            #self.text = pygame.render.Sprite(pygame.UPG.Renderer.load_texture(self.text))
            #self.text2 = pygame.render.Sprite(pygame.UPG.Renderer.load_texture(self.text2))

        self.RenderReady = False
    def onChange(self):
        pygame.UPG.Audio.playBGM(self.map_1['bgm'])
        
    def onChangeDone(self):
        self.RenderReady = True
        

    def graphicsUpdate(self):

        #self.SpriteGroup.update(pygame.time.get_ticks()/12)

        if not self.RenderReady:
            return
        
        if (pygame.UPG.RenderEnabled):

            #Render真的是太兇猛了
            for i in self.map_imgRendered:
                i.pos = (-self.camera_x, -self.camera_y)
            
            self.map_imgRendered[0].render()
            self.map_imgRendered[1].render()

            #SDL2中相對比較浪費資源的Surface 嘖嘖嘖...
            #ScreenBuffer = pygame.Surface((1280,720), pygame.SRCALPHA)
            ##self.SpriteGroup.draw(ScreenBuffer)
            self.character.update(pygame.time.get_ticks()/12)
            self.character.draw()

            #上層圖層
            self.map_imgRendered[2].render()

            #UI
            self.Render_Chat.update()
            self.Render_Chat.draw()
            
            #self.text.render((0,32))
            #self.text2.render((0,64))
            
        #else:

        #    screen_map = [Map_Render.camera_adjust(self.map_img[0], self.camera_x, self.camera_y),
        #        Map_Render.camera_adjust(self.map_img[1], self.camera_x, self.camera_y),
        #        Map_Render.camera_adjust(self.map_img[2], self.camera_x, self.camera_y)]
        #            
        #    pygame.UPG.Screen.blit(screen_map[0], (0,0))
        #    pygame.UPG.Screen.blit(screen_map[1], (0,0))

        #    self.SpriteGroup.draw(pygame.UPG.Screen)
            
        #    pygame.UPG.Screen.blit(screen_map[2], (0,0))

        #    self.SpriteGroupUI.draw(pygame.UPG.Screen)
        #    pygame.UPG.Screen.blit(text, (0,32))
        #    pygame.UPG.Screen.blit(text2, (0,64))
        
    def update(self):
        if not self.RenderReady:
            return
        #mouse1, mouse2 , mouse3 = Game_System.mouse_button
 
        cur_x, cur_y = pygame.mouse.get_pos()

        buttons = pygame.key.get_pressed()

        #if (Game_System.Event_Handler.Current_Event == None):
        if (buttons[K_LEFT]):
            self.character.row = 1
                    
            if (not self.LastButtons[K_LEFT]):
                self.character.freset()

            if (self.character.rect.x > 0):
                self.character.rect.x -= 8
            elif (self.camera_x > 0):
                self.camera_x -= 8
                    
        elif (buttons[K_RIGHT]):
            self.character.row = 2
            if (not self.LastButtons[K_RIGHT]):
                self.character.freset()
                    
            if (self.character.rect.x + self.character.frame_width < 1280):
                self.character.rect.x += 8
            elif (self.camera_x < self.map_1['x']*32-1280):
                self.camera_x += 8
                    
        if (buttons[K_UP]):
            self.character.row = 3
                    
            if (not self.LastButtons[K_UP]):
                self.character.freset()

            if (self.character.rect.y > -self.character.frame_height/2):
                    self.character.rect.y -= 8
            elif (self.camera_y > 0):
                self.camera_y -= 8
                    
        elif (buttons[K_DOWN]):
            self.character.row = 0
            if (not self.LastButtons[K_DOWN]):
                self.character.freset()
                    
            if (self.character.rect.y + self.character.frame_height < 720):
                self.character.rect.y += 8
            elif (self.camera_y < self.map_1['y']*32-720):
                self.camera_y += 8


        #bg
        '''
        if (buttons[K_LEFT] and self.camera_x > 0):
            if (buttons[K_LSHIFT]):
                self.camera_x -=10
            else:
                self.camera_x -=2
        elif (buttons[K_RIGHT]):
            if (buttons[K_LSHIFT]):
                self.camera_x +=10
            else:
                self.camera_x +=2
        if (buttons[K_UP] and self.camera_y > 0):
            if (buttons[K_LSHIFT]):
                self.camera_y -=10
            else:
                self.camera_y -=2
        elif (buttons[K_DOWN]):
            if (buttons[K_LSHIFT]):
                self.camera_y +=10
            else:
                self.camera_y +=2
        '''
        #if (Game_System.mouse_button_trigger[0]):
        #    Game_System.Window_Chat.add_text((str(cur_x)+","+str(cur_y)))
        #    Game_System.Window_Chat.add_text("aa")


        #if (Game_System.mouse_button_trigger[2]):
        #    import Events.Event_001
        #    Game_System.Event_Handler.Run_Event(Events.Event_001.Event_001())

        self.graphicsUpdate()
        self.LastButtons = buttons


