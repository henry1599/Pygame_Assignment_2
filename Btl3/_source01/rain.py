import pygame as pg
import random
from setting import *

class Rain(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('../_levels/png/rain01.png')
        self.image.set_alpha(random.randint(50, 255))
        self.rect = self.image.get_rect()
        self.speedx = -5
        self.speedy = random.randint(20,30)
        self.rect.x = random.randint(-100, screen_width + 100)
        self.rect.y = random.randint(-screen_height, -5)

    def update(self):
        
        if self.rect.bottom > screen_height:
            self.speedx = -5
            self.speedy = random.randint(20,30)
            self.rect.x = random.randint(-100, screen_width + 100)
            self.rect.y = random.randint(-screen_height, -5)
            
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy     