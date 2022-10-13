import pygame as pg
from helper import *
from setting import *

class Player(pg.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.getAssets()
        self.frame_idx = 0
        self.image = self.animations[State.IDLE()][self.frame_idx]
        self.image = pg.transform.scale(self.image, (player_sizes[State.IDLE()][0] * player_scale, player_sizes[State.IDLE()][1] * player_scale))
        self.rect = self.image.get_rect(topleft = position)
        self.state = State.IDLE()
        self.facing_right = True
        self.on_ground = False 
        self.on_left = False
        self.on_right = False
        self.on_ceiling = False
        self.is_attacking = False
        self.attack_idx = 0
        self.attack_buffer = 1.5
        self.attack_buffer_counter = 1.5

        # move
        self.direction = pg.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16
    
    def getAssets(self):
        path = '../_assets/Character/'
        self.animations = {
            State.IDLE() : [],
            State.RUN() : [],
            State.JUMP() : [],
            State.FALL() : [],
            State.ATTACK01() : [],
            State.ATTACK02() : [],
            State.ATTACK03() : []
        }
        
        self.attack_states = [
            State.ATTACK01(),
            State.ATTACK02(),
            State.ATTACK03()
        ]
        
        for animation in self.animations.keys():
            # print(animation.value)
            full_path = path + animation
            self.animations[animation] = readFolder(full_path)
    
    def animate(self):
        animation = self.animations[self.state]
        
        self.frame_idx += player_anim_speed[self.state]
        if self.frame_idx >= len(animation):
            self.frame_idx = 0
            if self.is_attacking:
                self.is_attacking = False
        
        image = animation[int(self.frame_idx)]
        image = pg.transform.scale(image, (player_sizes[self.state][0] * player_scale, player_sizes[self.state][1] * player_scale))
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pg.transform.flip(image, True, False)
            self.image = flipped_image
        
        if self.is_attacking:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
    
    def gatherInput(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0 

        if keys[pg.K_c] and not self.is_attacking and self.on_ground:
            self.attack()
            self.direction.x = 0
        if keys[pg.K_SPACE] and self.on_ground:
            self.jump()
    
    def getState(self):
        if self.is_attacking:
            self.state = self.attack_states[self.attack_idx]
        elif self.direction.y < 0:
            self.state = State.JUMP()
        elif self.direction.y > self.gravity + 0.1:
            self.state = State.FALL()
        else:
            if self.direction.x != 0:
                self.state = State.RUN()
            else:
                self.state = State.IDLE()
    
    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y = self.jump_speed

    def countdownAttackBuffer(self, delta_time):
        if self.attack_buffer_counter > 0:
            self.attack_buffer_counter -= delta_time
        else:
            self.attack_idx = 0
            self.attack_buffer_counter = self.attack_buffer
            
            
    
    def attack(self):
        self.frame_idx = 0
        self.is_attacking = True
        self.direction.y = 0
        self.attack_buffer_counter = self.attack_buffer
        self.attack_idx += 1
        self.attack_idx %= len(self.attack_states)

    def update(self, delta_time):
        self.countdownAttackBuffer(delta_time)
        self.gatherInput()
        self.getState()
        self.animate()