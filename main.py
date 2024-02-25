import pygame as pg
from pygame.mixer import music
from important_funcs import size, load_img, terminate, FPS
from camera import Camera


pg.init()
w, h = size
camera = Camera()
all_sprites = pg.sprite.Group()
scr = pg.display.set_mode(size)

