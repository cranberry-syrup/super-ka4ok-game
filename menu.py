import pygame as pg
from pygame.mixer import music
from pickle import load
from important_funcs import size, FPS, load_img, terminate, font_path


class Menu:
    def __init__(self):
        pg.init()
        self.scr = pg.display.set_mode(size)
        music.load('assets/audio/menu.mp3')
        music.play()
        self.font_big = pg.font.Font(font_path, 30)
        self.backg = pg.transform.scale(load_img('assets/sprites/backg.jpg'), size)

