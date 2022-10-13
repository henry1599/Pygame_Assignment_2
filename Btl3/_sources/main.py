import pygame as pg 
import sys     
from setting import *
from level import Level

pg.init()

screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() 
            sys.exit()
            
    level.run()
    
    pg.display.update()
    clock.tick(60)