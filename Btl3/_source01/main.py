import pygame as pg 
import sys     
from setting import *
from level import Level
from level_data import level_0

pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
level = Level(level_0, screen)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() 
            sys.exit()
            
    screen.fill('black')
    level.run()
    
    pg.display.update()
    clock.tick(60)