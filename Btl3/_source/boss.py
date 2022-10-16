import pygame as pg
import random
from helper import *
from setting import *
from particle import *
from math import sin
from audio import *
from ultimate import *

class AttackField(pg.sprite.Sprite):
    def __init__(self, boss, player):
        super().__init__()
        self.image = pg.image.load('../_assets/boss/field_of_attack/rect.png').convert_alpha()
        self.boss = boss
        self.player = player
        self.rect = self.image.get_rect(center = (screen_width / 2 - 150, 650))
        self.image = pg.transform.scale(self.image, (600, 150))
    
    def update(self):
        if self.boss.is_dealing_range_attack:
            collide = pg.Rect.colliderect(self.rect, self.player.rect)
            if collide:
                self.player.get_damage(-20)
        if self.boss.is_dealing_special_attack:
            collide = pg.Rect.colliderect(self.rect, self.player.rect)
            if collide:
                self.player.get_damage(-35)

class Boss(pg.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.getAssets()
        self.state = State.LIE_STATIC()
        self.frame_idx = 0
        self.image = self.animations[self.state][self.frame_idx]
        self.image = pg.transform.scale(self.image, (boss_sizes[self.state][0] * boss_scale, boss_sizes[self.state][1] * boss_scale))
        self.rect = self.image.get_rect(topleft = boss_init_position)
        self.facing_right = True
        self.is_wakeup = False
        self.position = boss_init_position
        self.player = player
        
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
        self.attack_idx = -1
        self.is_moving = False
        
        self.is_dealing_melee_attack = False
        self.is_dealing_range_attack = False
        self.is_dealing_special_attack = False
    
    def getAssets(self):
        path_Light = '../_assets/boss/'
        self.animations = {
            State.IDLE() : [],
            State.RUN() : [],
            State.ATTACK01() : [],
            State.ATTACK02() : [],
            State.ATTACK03() : [],
            State.AWAKE() : [],
            State.LIE_STATIC() : [],
            State.NOT_ATTACK() : []
        }
        
        for animation in self.animations.keys():
            # print(animation.value)
            full_path = path_Light + animation
            self.animations[animation] = readFolder(full_path)
        
        for value in self.animations.values():
            print(len(value))
    
    def resetDealingDamage(self):
        self.is_dealing_melee_attack = False
        self.is_dealing_range_attack = False
        self.is_dealing_special_attack = False
    
    def animate(self):
        animation = self.animations[self.state]
        self.frame_idx += boss_anim_speed[self.state]
        # print(len(animation))
        # print(self.frame_idx)
        if self.state == State.ATTACK01():
            if self.frame_idx >= 10:
                self.is_dealing_melee_attack = True
        if self.state == State.ATTACK02():
            if 10 <= self.frame_idx < 15:
                self.is_dealing_range_attack = True
        if self.state == State.ATTACK03():
            if 32 <= self.frame_idx < 38:
                self.is_dealing_special_attack = True
        if self.frame_idx >= len(animation):
            self.frame_idx = 0
            self.resetDealingDamage()
            if self.state == State.ATTACK01() or self.state == State.ATTACK02() or self.state == State.ATTACK03() or self.state == State.NOT_ATTACK():
                self.is_attacking = False
                self.state = State.IDLE()
            if not boss_anim_loop[self.state]:
                self.state = State.IDLE()
            if self.state == State.AWAKE():
                self.state = State.IDLE()
        # else:
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
    
    def get_movement_data(self, currentx, currenty, targetx, targety):
        start = pg.math.Vector2(currentx, currenty)
        end = pg.math.Vector2(targetx, targety)
        new_vec = end - start
        if new_vec.length() == 0: return new_vec
        else: return new_vec.normalize()
    
    def attack(self, attackIdx, position, facing, perform, time):
        direction = self.get_movement_data(self.rect.centerx, self.rect.centery, position[0], position[1])
        if abs(self.position[0] - position[0]) <= 55:
            direction = pg.math.Vector2(0, 0)
        self.position += direction * 50
        self.rect.center = self.position
        self.facing_right = True if facing == 1 else False
        remaining_time = pg.time.get_ticks() - self.attack_start_time
        if remaining_time >= time:
            self.endattack()
            
        # * attack code goes bruhhhhhhhhhhh
        if not perform:
            return 
        if attackIdx == 1:
            self.state = State.ATTACK01()
        elif attackIdx == 2:
            self.state = State.ATTACK02()
        elif attackIdx == 3:
            self.state = State.ATTACK03()
        elif attackIdx == 4:
            self.state = State.NOT_ATTACK()
        
    
    def endattack(self):
        self.is_attacking = False
    
    def update(self, delta_time):
        keys = pg.key.get_pressed()
        self.animate()
        
        if self.is_dealing_melee_attack:
            collide = pg.Rect.colliderect(self.rect, self.player.rect)
            if collide:
                self.player.get_damage(-10)
        
        if self.is_wakeup:
            if self.state == State.IDLE():
                if not self.is_attacking:
                    self.attack_idx = random.randint(1, 4)
                else:
                    self.attack_idx = -1
            
                if self.attack_idx != -1 and not self.is_attacking:
                    self.attack_start_time = pg.time.get_ticks() + 2000
                    self.is_attacking = True
                    self.is_moving = True
                    
                    self.frame_idx = 0
                    attackString = 'attack ' + str(self.attack_idx)
                    attack_state_idx = random.randint(0, 2)
                    self.attack_position = boss_attack_state[attackString][attack_state_idx]['position']
                    self.attack_facing = boss_attack_state[attackString][attack_state_idx]['facing']
                    self.attack_perform = boss_attack_state[attackString][attack_state_idx]['attack']
                    self.attack_time = boss_attack_state[attackString][attack_state_idx]['time']
                        
                
            if self.is_attacking:
                self.attack(self.attack_idx, self.attack_position, self.attack_facing, self.attack_perform, self.attack_time)
            
            
        
        if keys[pg.K_v] and not self.is_wakeup:
            self.is_wakeup = True
            self.wakeup()
            