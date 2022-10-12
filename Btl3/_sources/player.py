import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pg.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = position)

        self.direction = pg.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -12
    
    def gatherInput(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0 

        if keys[pg.K_SPACE]:
            self.jump()
    
    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y = self.jump_speed
    
    def update(self):
        self.gatherInput()