import pygame as pg 
import sys     
from setting import *
from rain import *
from level import Level
import time
import random
from level_data import level_0

pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
level = Level(level_0, screen)

# rain setup
rain_group = pg.sprite.Group()
for i in range(200):
    rain = Rain()
    rain_group.add(rain)

thunderstorm = thunderstorm_color
is_thunder = False

light_scale = 3
light = pg.image.load('../_assets/light.png').convert_alpha()
light = pg.transform.scale(light, (light.get_size()[0] * light_scale, light.get_size()[1] * light_scale))
light_rect = light.get_rect(bottomright = (0, 0))
dark_value = 230

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() 
            sys.exit()
    
    rain_group.update()
    level.run()
    rain_group.draw(screen)

    filter = pg.surface.Surface((screen_width, screen_height))
    filter.fill(pg.color.Color(dark_value, dark_value, dark_value, 255))
    light_rect = light.get_rect(bottomright = (level.player.sprite.rect.centerx, level.player.sprite.rect.centery))
    light_position = light_rect.center
    filter.blit(light, light_position, special_flags=pg.BLEND_RGBA_SUB)
    screen.blit(filter, (0, 0), special_flags=pg.BLEND_RGBA_SUB)
    # pg.display.flip()
        
    pg.display.update()
    clock.tick(60)