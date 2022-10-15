import pygame as pg 
import sys     
from setting import *
from rain import *
from level import Level
from level_data import *
from light import *
from overworld import *
from ui import *
from audio import *

class Game:
    def __init__(self):
        self.max_level = 1
        self.max_health = 100
        self.current_health = self.max_health
        self.coins = 0
        
        self.ui = UI(screen)
        
        self.overworld = Overworld(0, self.max_level, screen, self.create_level)
        self.status = GameState.OVERWORLD()
        
        self.loadSound()
        self.initVolume()
        
        self.SFX[SFXType.OVERWORLD_THEME()].playloop()
        self.SFX[SFXType.LEVEL_THEME()].stop()
        self.SFX[SFXType.RAIN()].stop()
    
    def loadSound(self):
        self.SFX = {
            SFXType.OVERWORLD_THEME() : SFX('../_audio/overworld_theme.wav'),
            SFXType.LEVEL_THEME() : SFX('../_audio/normal_level_theme.wav'),
            SFXType.RAIN() : SFX('../_audio/rain.wav')
        }
    
    def initVolume(self):
        self.SFX[SFXType.OVERWORLD_THEME()].set_volume(0.5)
        self.SFX[SFXType.LEVEL_THEME()].set_volume(0.65)
        self.SFX[SFXType.RAIN()].set_volume(0.55)
    
    def create_overworld(self, current_level, new_max_level):
        if new_max_level >= self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level)
        self.status = GameState.OVERWORLD()
        self.SFX[SFXType.OVERWORLD_THEME()].playloop()
        self.SFX[SFXType.LEVEL_THEME()].stop()
        self.SFX[SFXType.RAIN()].stop()
    
    def create_level(self, current_level):
        self.level = Level(current_level, screen, self.create_overworld, self.update_coins, self.update_health)
        self.status = GameState.LEVEL()
        self.SFX[SFXType.OVERWORLD_THEME()].stop()
        self.SFX[SFXType.LEVEL_THEME()].playloop()
        self.SFX[SFXType.RAIN()].playloop()
    
    def update_coins(self, amount):
        self.coins += amount
    
    def update_health(self, amount):
        self.current_health += amount
    
    def check_game_over(self):
        if self.current_health <= 0:
            self.level.killallsoudns()
            self.current_health = 100
            self.coins = 0
            self.overworld = Overworld(0, self.max_level, screen, self.create_level)
            self.status = GameState.OVERWORLD()
    
    def run(self):
        if self.status == GameState.OVERWORLD():
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(self.current_health, self.max_health)
            self.ui.show_coin(self.coins)
            self.check_game_over()

pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
game = Game()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() 
            sys.exit()
    
    screen.fill('black')
    game.run()
    
    pg.display.update()
    clock.tick(60)