import pygame, random, os, time
from pygame.locals import *
from Constants import *
from components import *

class Goal(SpriteRenderer):
    def __init__(self, 
                 screen,
                 image_path : str, 
                 position : tuple = (0, 0), 
                 scale : tuple = (1, 1), 
                 scale_multiplier : float = 1, 
                 anchor : Anchor = Anchor.TOP_LEFT,
                 angle_delta_min = 1,
                 angle_delta_max = 4,
                 bounceable_group = None,
                 player = 0):
        super().__init__(screen, image_path, position, scale, scale_multiplier, anchor, angle_delta_min, angle_delta_max)
        self.player = player
        self.bounceable_group = bounceable_group
    def update(self):
        if pygame.sprite.spritecollide(self, self.bounceable_group, False):        
            return True
        else:
            return False

    def draw(self):
        super().draw()