import pygame, random, os, time
from pygame.locals import *
from Constants import *
from components import *

class Ball(SpriteRenderer):
    def __init__(self, 
                 screen,
                 image_path : str, 
                 position : tuple = (0, 0), 
                 scale : tuple = (1, 1), 
                 scale_multiplier : float = 1, 
                 anchor : Anchor = Anchor.TOP_LEFT,
                 angle_delta_min = 1,
                 angle_delta_max = 4,
                 init_speed : tuple = (3, 3),
                 bounceable_group = None):
        super().__init__(screen, image_path, position, scale, scale_multiplier, anchor, angle_delta_min, angle_delta_max)
        self.x_speed = init_speed[0]
        self.y_speed = init_speed[1]
        self.x_dir = Direction.LEFT
        self.y_dir = Direction.UP
        if self.x_speed > 0:
            self.x_dir = Direction.RIGHT
        if self.y_speed > 0:
            self.y_dir = Direction.DOWN
        self.is_into_hold = False
        self.bounceable_group = bounceable_group

    def update(self):
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed
        
        # * Collide Down
        # * Switch signed of y_speed when colliding top-down
        if self.rect.bottom >= HEIGHT:
            self.y_speed *= -1
            self.y_dir = Direction.UP
        
        # * Collide Up
        # * Switch signed of y_speed when colliding top-down
        if self.rect.top <= 0:
            self.y_speed *= -1
            self.y_dir = Direction.DOWN
            
        # * Side
        # * Switch signed of x_speed when colliding top-down
        if self.rect.left <= 0:
            self.x_speed *= -1
            self.x_dir = Direction.RIGHT
            
        if self.rect.right >= WIDTH:
            self.x_speed *= -1
            self.x_dir = Direction.LEFT
            
        # * Terrible collision checker
        if self.bounceable_group is not None:
            hits = []
            for block in pygame.sprite.spritecollide(self, self.bounceable_group, False):
                clip = self.rect.clip(block.rect)
                hits = [edge for edge in ['bottom', 'top', 'left', 'right'] if getattr(clip, edge) == getattr(self.rect, edge)]
                # * Bottom left
                if set(COLLIDE_INFO['BL']).issubset(hits):
                    if self.x_dir == Direction.LEFT and self.y_dir == Direction.DOWN:
                        if random.randint(0, 1) == 0:
                            self.y_speed *= -1
                            self.y_dir = Direction.UP
                        else:
                            self.x_speed *= -1
                            self.x_dir = Direction.RIGHT
                    elif self.x_dir == Direction.LEFT and self.y_dir == Direction.UP:
                        self.x_speed *= -1
                        self.x_dir = Direction.RIGHT
                    elif self.x_dir == Direction.RIGHT and self.y_dir == Direction.DOWN:
                        self.y_speed *= -1
                        self.y_dir = Direction.UP
                # * Bottom Left Right
                elif set(COLLIDE_INFO['BLR']).issubset(hits):
                    if self.x_dir == Direction.LEFT and self.y_dir == Direction.DOWN:
                        self.y_speed *= -1
                        self.y_dir = Direction.UP
                    elif self.x_dir == Direction.RIGHT and self.y_dir == Direction.DOWN:
                        self.y_speed *= -1
                        self.y_dir = Direction.UP
                # * Bottom Right
                elif set(COLLIDE_INFO['BR']).issubset(hits):
                    if self.x_dir == Direction.RIGHT and self.y_dir == Direction.DOWN:
                        if random.randint(0, 1) == 0:
                            self.y_speed *= -1
                            self.y_dir = Direction.UP
                        else:
                            self.x_speed *= -1
                            self.x_dir = Direction.LEFT
                    elif self.x_dir == Direction.RIGHT and self.y_dir == Direction.UP:
                        self.x_speed *= -1
                        self.x_dir = Direction.LEFT
                    elif self.x_dir == Direction.LEFT and self.y_dir == Direction.DOWN:
                        self.y_speed *= -1
                        self.y_dir = Direction.UP
                # * Bottom Right Top
                elif set(COLLIDE_INFO['BRT']).issubset(hits):
                    if self.x_dir == Direction.RIGHT and self.y_dir == Direction.DOWN:
                        self.x_speed *= -1
                        self.x_dir = Direction.LEFT     
                    elif self.x_dir == Direction.RIGHT and self.y_dir == Direction.UP:
                        self.x_speed *= -1
                        self.x_dir = Direction.RIGHT
                # * Top Right
                elif set(COLLIDE_INFO['TR']).issubset(hits):
                    if self.x_dir == Direction.RIGHT and self.y_dir == Direction.UP:
                        if random.randint(0, 1):
                            self.y_speed *= -1
                            self.y_dir = Direction.DOWN
                        else:
                            self.x_speed *= -1
                            self.x_dir = Direction.LEFT
                    elif self.x_dir == Direction.RIGHT and self.y_dir == Direction.DOWN:
                        self.x_speed *= -1
                        self.x_dir = Direction.LEFT 
                    elif self.x_dir == Direction.LEFT and self.y_dir == Direction.UP:
                        self.y_speed *= -1
                        self.y_dir = Direction.DOWN
                # * Top Left Right
                elif set(COLLIDE_INFO['TLR']).issubset(hits):
                    if self.x_dir == Direction.RIGHT and self.y_dir == Direction.UP:
                        self.y_speed *= -1
                        self.y_dir = Direction.DOWN
                    elif self.x_dir == Direction.LEFT and self.y_dir == Direction.UP:
                        self.y_speed *= -1
                        self.y_dir = Direction.DOWN
                # * Top Left
                elif set(COLLIDE_INFO['TL']).issubset(hits):
                    if self.x_dir == Direction.LEFT and self.y_dir == Direction.UP:
                        if random.randint(0, 1):
                            self.x_speed *= -1
                            self.x_dir == Direction.RIGHT
                        else:
                            self.y_speed *= -1
                            self.y_dir = Direction.DOWN
                    elif self.x_dir == Direction.RIGHT and self.y_dir == Direction.UP:
                        self.y_speed *= -1
                        self.y_dir = Direction.DOWN 
                    elif self.x_dir == Direction.LEFT and self.y_dir == Direction.DOWN:
                        self.x_speed *= -1
                        self.x_dir = Direction.RIGHT
                # * Bottom Top Left
                elif set(COLLIDE_INFO['BTL']).issubset(hits):
                    if self.x_dir == Direction.LEFT and self.y_dir == Direction.DOWN:
                        self.x_speed *= -1
                        self.x_dir = Direction.RIGHT 
                    elif self.x_dir == Direction.LEFT and self.y_dir == Direction.UP:
                        self.x_speed *= -1
                        self.x_dir = Direction.RIGHT
                            
        
    def draw(self):
        super().draw()
    
    def draw_with_rotation(self):
        # * Use for static object ONLY
        # * Dynamic object won't work
        super().draw_with_rotation();
    
    