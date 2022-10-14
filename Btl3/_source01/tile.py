import pygame as pg
from level_data import *
from setting import *

class Tile(pg.sprite.Sprite):
    def __init__(self, size, x, y, type):
        super().__init__()
        self.image = pg.Surface((size, size))
        self.image.fill('grey')
        self.image = pg.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect(topleft = (x, y))