import pygame as pg
from tile import Tile 
from setting import tile_size, screen_width
from player import *

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setupLevel(level_data)
        self.world_offset = 0

    def setupLevel(self, layout):
        self.tiles = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()
        
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x_pos = col_index * tile_size
                y_pos = row_index * tile_size
                pos = (x_pos, y_pos)
                if col == 'X':
                    tile = Tile(pos, tile_size)
                    self.tiles.add(tile)
                if col == 'P':
                    player = Player(pos)
                    self.player.add(player)
                    
    def scroll_horizontally(self):
        player = self.player.sprite    
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_offset = 5
            player.speed = 0
        elif player_x > screen_width * 3 / 4 and direction_x > 0:
            self.world_offset = -5
            player.speed = 0
        else:
            self.world_offset = 0
            player.speed = 5
    
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
    
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.applyGravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
    
    def run(self):
        self.tiles.update(self.world_offset)
        
        self.tiles.draw(self.display_surface)
        self.scroll_horizontally()

        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
