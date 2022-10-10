from turtle import pos, position
import pygame, random, os, time
from pygame.locals import *
from Constants import *
from components import *
import numpy as np

class Player(SpriteRenderer):
    def __init__(self, 
                 screen,
                 image_path : str, 
                 position : tuple = (0, 0), 
                 scale : tuple = (1, 1), 
                 speed : float = 3.0,
                 scale_multiplier : float = 1, 
                 anchor : Anchor = Anchor.TOP_LEFT,
                 angle_delta_min = 1,
                 angle_delta_max = 4,
                 bounceable_group = None):
        super().__init__(screen, image_path, position, scale, scale_multiplier, anchor, angle_delta_min, angle_delta_max)
        self.speed = speed

    def moverment(self, direction):
        ## normalize direction vector
        cost = list(map(lambda x: x**2, direction))
        direction = direction / np.sqrt(np.sum(cost)) 
        ## check if can not move
        new_min_x = self.rect.left + direction[0] * self.speed
        new_max_x = self.rect.right + direction[0] * self.speed
        new_min_y = self.rect.top + direction[1] * self.speed
        new_max_y = self.rect.bottom + direction[1] * self.speed

        if (new_min_x == 0) or (new_min_x == WIDTH / 2) or (new_max_x == WIDTH / 2) or (new_max_x == WIDTH):
            direction[0] = 0
        if (new_min_y == 0) or (new_min_y == HEIGHT / 2) or (new_max_y == HEIGHT / 2) or (new_max_y == HEIGHT):
            direction[1] = 0
        ## update position
        pos_x = self.position[0] + direction[0] * self.speed
        pos_y = self.position[1] + direction[1] * self.speed
        
        
        
        self.position = (pos_x, pos_y)
        self.rect.x = pos_x 
        self.rect.y = pos_y

    def draw(self):
        super().draw()
