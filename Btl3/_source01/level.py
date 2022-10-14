import pygame as pg
from level_data import *
from helper import *
from setting import *
from tile import *

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface 
        
        terrain_layout = readCSVLayout(level_data[LevelType.TERRAIN()])
        self.terrain_sprites = self.createTileGroup(terrain_layout, LevelType.TERRAIN())
    
    def createTileGroup(self, layout, type):
        sprite_group = pg.sprite.Group()

        for row_idx, row in enumerate(layout):
            for col_idx, value in enumerate(row):
                if value != '-1':
                    x = col_idx * tile_size
                    y = row_idx * tile_size
                    
                    if type == LevelType.TERRAIN():
                        sprite = Tile(tile_size, x, y, type)
                        sprite_group.add(sprite)
        
        return sprite_group
    
    def run(self):
        self.terrain_sprites.draw(self.display_surface)