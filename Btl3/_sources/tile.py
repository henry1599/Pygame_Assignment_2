import pygame as pg
from setting import *
from player import *

class Tile(pg.sprite.Sprite):
    def __init__(self, position, size, color):
        super().__init__()
        self.image = pg.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = position)
    
    def changeColor(self, color):
        self.image.fill(color)
    
    def update(self, player, x_offset = 0, y_offset = 0):
        self.changeColor(level_theme[player.type]['tile'])
        self.rect.x += x_offset
        self.rect.y += y_offset