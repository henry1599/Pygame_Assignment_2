import pygame as pg
from tile import Tile 
from setting import tile_size, screen_width
from player import *
import time

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setupLevel(level_data)
        self.world_offset_x = 0
        self.world_offset_y = 0
        self.current_x = 0
        self.old_time = time.time()
        self.delta_time = 0
        self.clock = pg.time.Clock()

    def setupLevel(self, layout):
        self.tiles = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()
        
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x_pos = col_index * tile_size
                y_pos = row_index * tile_size
                pos = (x_pos, y_pos)
                if col == 'X':
                    tile = Tile(pos, tile_size, level_theme[PlayerType.LIGHT()]['tile'])
                    self.tiles.add(tile)
                if col == 'P':
                    player = Player(pos, self.display_surface)
                    self.player.add(player)
                    
    def scroll_horizontally(self):
        player = self.player.sprite    
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_offset_x = 5
            player.speed = 0
        elif player_x > screen_width * 3 / 4 and direction_x > 0:
            self.world_offset_x = -5
            player.speed = 0
        else:
            self.world_offset_x = 0
            player.speed = 5
    
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False
    
    def vertical_movement_collision(self):
        player = self.player.sprite
        if not player.is_attacking and not player.is_transforming:
            player.applyGravity()
        else:
            return

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    # if not player.is_attacking:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    # if not player.is_attacking:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > player.gravity + 0.1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False
    
    def run(self):
        # update delta time
        now = time.time()
        self.delta_time = now - self.old_time
        self.old_time = now
        self.display_surface.fill(level_theme[self.player.sprite.type]['background'])
        self.tiles.update(self.player.sprite, self.world_offset_x, self.world_offset_y)
        
        self.tiles.draw(self.display_surface)
        self.scroll_horizontally()
        # self.scroll_vertically()

        self.player.update(self.delta_time)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
