import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pg.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = position)
    
    def update(self, x_offset = 0):
        self.rect.x += x_offset