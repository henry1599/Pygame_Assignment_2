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
        ## update position
        pos_x = self.position[0] + direction[0] * self.speed
        pos_y = self.position[1] + direction[1] * self.speed
        self.position =  (pos_x, pos_y)

    def draw(self):
        super().draw()
