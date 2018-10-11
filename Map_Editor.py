############ Map Editor ############
from random import randint
from pygame_Button_Old import pygame_Button
import pygame, os
import tkinter as tk
from tkinter import filedialog

from pygame.locals import *
#minxy = 40, 23
def save_map(path):
    with open(path, 'wb') as f:
        #XY界線與版本   
        f.write((128).to_bytes(2, byteorder='big'))
        f.write((128).to_bytes(2, byteorder='big'))
        f.write(bytes([1]))
        #地板貼圖名稱
        a1 = bytes("Outside_A2.png".encode())
        f.write(bytes([len(a1)]))
        f.write(a1)
        
        #遠景圖名稱
        a2 = bytes("bg.png".encode())
        f.write(bytes([len(a2)]))
        f.write(a2)

        #地圖名稱
        a3 = bytes("總之是野生的草原".encode())
        f.write(bytes([len(a3)]))
        f.write(a3)

        #BGM名稱
        a4 = bytes("1.mp3".encode())
        f.write(bytes([len(a4)]))
        f.write(a4)

        #地圖資料(圖層1)
        for i in range(128):
            add = []
            for j in range(128):
                add.append(1)

            f.write(bytes(add))

        #地圖資料(圖層2)
        for i in range(128):
            add = []
            for j in range(128):
                if (randint(1,10) > 8):
                    add.append(5)
                else:
                    add.append(0)
            f.write(bytes(add))

        #地圖資料(圖層3)
        for i in range(128):
            add = []
            for j in range(128):
                if (randint(1,10) > 8):
                    add.append(0)
                else:
                    add.append(0)
            f.write(bytes(add))
            
        f.close()
    
def load_map(path):
    with open(path, 'rb') as f:
        x,y,ver= int.from_bytes(f.read(2), 'big'), int.from_bytes(f.read(2), 'big'), f.read(1)
        header = []
        
        for i in range(4):
            str_size = f.read(1)[0]
            s = f.read(str_size)
            header.append(s.decode())

        mapdata = []
        for i in range(y):
            r = f.read(x)
            mapdata.append(r)

        mapdata2 = []
        for i in range(y):
            r = f.read(x)
            mapdata2.append(r)

        mapdata3 = []
        for i in range(y):
            r = f.read(x)
            mapdata3.append(r)
            
        mapinfo = {'x' : x, 'y' : y, 'ver' : ver,
                    'tileset' : header[0],
                    'bg' : header[1],
                    'name' : header[2],
                    'bgm' : header[3],
                    'layer1' : mapdata,
                    'layer2' : mapdata2,
                    'layer3' : mapdata3 }
        f.close()
    return mapinfo

filename = ""
mapfile = None
def open_file():
    global filename, mapfile
    filename = filedialog.askopenfilename(filetypes=(("Map File","*.map"),("all files","*.*"))  )
    if (not filename == ''):
        mapfile = load_map(filename)

def save_file():
    global filename
    a = filedialog.asksaveasfilename(filetypes=(("Map File","*.map"),("all files","*.*"))  )
    if (not a == ''):
        save_map(a)
        filename = a

appname = " Map Editor - FPS "
def create_window():
    global filename, cur_x, cur_y
    FPS = 60

    WINDOWWIDTH = 1280
    WINDOWHEIGHT = 720
    pygame.init()
    screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), pygame.HWSURFACE)

    SpriteGroup = pygame.sprite.Group()
    FPSCLOCK = pygame.time.Clock()

    root = tk.Tk()
    root.withdraw()

    ######
    btn_func1 = lambda: (print("New"))
    btn_1 = pygame_Button((60,30), "新建", btn_func1)
    btn_1.rect.x = 0
    btn_1.rect.y = 0

    SpriteGroup.add(btn_1)
    btn_func2 = lambda: (open_file(), print(filename), print(mapfile))
    btn_2 = pygame_Button((60,30), "讀取", btn_func2)
    btn_2.rect.x = 60
    btn_2.rect.y = 0
    SpriteGroup.add(btn_2)

    btn_func3 = lambda: (save_file(), print(filename))
    btn_3 = pygame_Button((60,30), "存檔", btn_func3)
    btn_3.rect.x = 120
    btn_3.rect.y = 0
    SpriteGroup.add(btn_3)
    ######
    cur_x, cur_y = 0,0
    while True:
        mouse_event = [False, False, False]
        # 退出事件處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                cur_x, cur_y = event.pos
                if (event.button == 1):
                    mouse_event[0] = True
                if (event.button == 2):
                    mouse_event[1] = True
                if (event.button == 3):
                    mouse_event[2] = True


        action = {'mouse_button' : mouse_event, 'mouse_axis': (cur_x,cur_y)}
        SpriteGroup.update(action)
        SpriteGroup.draw(screen)
        pygame.display.flip()
        FPSCLOCK.tick(FPS)
        pygame.display.set_caption(filename + appname + str(int(FPSCLOCK.get_fps())))


save_map('Maps//testmap.map')



create_window()
