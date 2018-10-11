######## Map Render ########
##each type is = 64*32
##each block = 32 * 32

tile_x, tile_y = 32, 32
import pygame

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

def select_type(tileset, n):
    rect = ( (n-1)*64, 0, 64, 96)
    return tileset.subsurface(rect)

def select_type2(src, n):
    rect = ( (n%2)*tile_x, int(n/2)*tile_y, tile_x, tile_y)
    return src.subsurface(rect)

def camera_adjust(src, posx, posy):
    return src.subsurface((posx, posy, 1280, 720))

def render_map(x):
    #bg = pygame.image.load(x['bg'])
    full_map = pygame.Surface((tile_x * x['x'], tile_y * x['y']))
    full_map2 = pygame.Surface((tile_x * x['x'], tile_y * x['y']), pygame.SRCALPHA)
    full_map3 = pygame.Surface((tile_x * x['x'], tile_y * x['y']), pygame.SRCALPHA)

    tileset = pygame.image.load("Tilesets/%s" % x['tileset']).convert_alpha()

    ###layer1
    for i in range(x['y']):
        for j in range(x['x']):            
            if (x['layer1'][i][j] > 0):
                a = select_type(tileset, x['layer1'][i][j])
                b = select_type2(a, 1)

                full_map.blit(b, (j*tile_x, i*tile_y))
                
            if (x['layer2'][i][j] > 0):
                a = select_type(tileset, x['layer2'][i][j])
                b = select_type2(a, 1)

                full_map2.blit(b, (j*tile_x, i*tile_y))
                
            if (x['layer3'][i][j] > 0):
                a = select_type(tileset, x['layer3'][i][j])
                b = select_type2(a, 0)

                full_map3.blit(b, (j*tile_x, i*tile_y))
                
    return (full_map, full_map2, full_map3)
