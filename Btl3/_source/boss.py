import pygame as pg
import random
from helper import *
from setting import *
from particle import *
from math import sin
from audio import *
from ultimate import *

class Boss(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.getAssets()
        self.state = State.LIE_STATIC()
        self.frame_idx = 0
        self.image = self.animations[self.state][self.frame_idx]
        self.image = pg.transform.scale(self.image, (boss_sizes[self.state][0] * boss_scale, boss_sizes[self.state][1] * boss_scale))
        self.rect = self.image.get_rect(topleft = boss_init_position)
        self.facing_right = True
        self.is_wakeup = False
        
        self.wait_move_interval_value = 3
        self.wait_move_interval = self.wait_move_interval_value
        self.move_speed = 8
        self.is_moving = False
        self.is_attacking = False

        self.attack_position = (0, 0)
        self.attack_facing = 1
        self.attack_perform = False
        self.attack_time = 0
        self.attack_start_time = 0
    
    
    def getAssets(self):
        path_Light = '../_assets/boss/'
        self.animations = {
            State.IDLE() : [],
            State.RUN() : [],
            State.ATTACK01() : [],
            State.ATTACK02() : [],
            State.ATTACK03() : [],
            State.AWAKE() : [],
            State.LIE_STATIC() : []
        }
        
        for animation in self.animations.keys():
            # print(animation.value)
            full_path = path_Light + animation
            self.animations[animation] = readFolder(full_path)
    
    def animate(self):
        animation = self.animations[self.state]
        self.frame_idx += boss_anim_speed[self.state]
        if self.frame_idx >= len(animation):
            if boss_anim_loop[self.state]:
                self.frame_idx = 0
            if self.state == State.AWAKE():
                # self.frame_idx = 0
                self.state = State.IDLE()
        else:
            image = animation[int(self.frame_idx)]
            image = pg.transform.scale(image, (boss_sizes[self.state][0] * boss_scale, boss_sizes[self.state][1] * boss_scale))

            if self.facing_right:
                self.image = image
            else:
                flipped_image = pg.transform.flip(image, True, False)
                self.image = flipped_image
    
    def wakeup(self):
        self.state = State.AWAKE()
        self.frame_idx =  0
        
    def attack(self, position, facing, perform, time):
        self.rect.center = position
        self.facing_right = True if facing == 1 else False
        remaining_time = pg.time.get_ticks() - self.attack_start_time
        if remaining_time >= time:
            self.endattack()

        # attack code goes bruhhhhhhhhhhh
        
    
    def endattack(self):
        self.is_attacking = False
    
    def update(self, delta_time):
        keys = pg.key.get_pressed()
        self.animate()
        
        if self.is_wakeup:
            if self.state == State.IDLE():
                if not self.is_attacking:
                    attackIdx = random.randint(1, 3)
                else:
                    attackIdx = -1
            
                if attackIdx != -1 and not self.is_attacking:
                    self.attack_start_time = pg.time.get_ticks()
                    self.is_attacking = True
                    
                    attackString = 'attack ' + str(attackIdx)
                    attack_state_idx = random.randint(0, 2)
                    self.attack_position = boss_attack_state[attackString][attack_state_idx]['position']
                    self.attack_facing = boss_attack_state[attackString][attack_state_idx]['facing']
                    self.attack_perform = boss_attack_state[attackString][attack_state_idx]['attack']
                    self.attack_time = boss_attack_state[attackString][attack_state_idx]['time']
                
                if self.is_attacking:
                    self.attack(self.attack_position, self.attack_facing, self.attack_perform, self.attack_time)
            
            
        
        if keys[pg.K_v] and not self.is_wakeup:
            self.is_wakeup = True
            self.wakeup()
            