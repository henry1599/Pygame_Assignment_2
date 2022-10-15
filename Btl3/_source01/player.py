import pygame as pg
from helper import *
from setting import *
from particle import *
from math import sin
from audio import *

class Player(pg.sprite.Sprite):
    def __init__(self, position, surf, update_health, update_light):
        super().__init__()
        self.display_surf = surf
        self.getAssets()
        self.frame_idx = 0
        self.type = PlayerType.LIGHT()
        self.image = self.animations_Light[State.IDLE()][self.frame_idx]
        self.image = pg.transform.scale(self.image, (player_sizes[self.type][State.IDLE()][0] * player_scale, player_sizes[self.type][State.IDLE()][1] * player_scale))
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
        self.is_transforming = False
        
        self.update_health = update_health
        self.update_light = update_light
        self.update_light(False)

        # move
        self.direction = pg.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -8.0
        self.max_jump_speed = -11.0
        self.jump_buffer = -1.0
        self.get_peak = False
        
        self.particle = pg.sprite.GroupSingle()
        particle = VFX_Transform(position, self.type, self)
        self.particle.add(particle)
        
        self.is_invincible = False
        self.invinciblity_duration = 750
        self.hurt_time = 0
        
        self.loadSound()
        self.initVolume()
        
        self.SFX[SFXType.RUN()].playloop()
    
    def loadSound(self):
        self.SFX = {
            SFXType.RUN() : SFX('../_audio/run.wav'),
            SFXType.JUMP() : SFX('../_audio/jump.wav'),
            SFXType.SWORD() : SFX('../_audio/sword_splash.wav'),
            SFXType.HIT() : SFX('../_audio/player_hit_by_enemy.wav')
        }
    
    def initVolume(self):
        self.SFX[SFXType.RUN()].set_volume(0.25)
        self.SFX[SFXType.JUMP()].set_volume(0.6)
        self.SFX[SFXType.SWORD()].set_volume(0.75)
        self.SFX[SFXType.HIT()].set_volume(0.75)
    
    def killallsounds(self):
        for val in self.SFX.values():
            val.stop()
    
    def getAssets(self):
        path_Light = '../_assets/Character/'
        path_Dark = '../_assets/Dark/Dark/'
        self.animations_Light = {
            State.IDLE() : [],
            State.RUN() : [],
            State.JUMP() : [],
            State.FALL() : [],
            State.ATTACK01() : [],
            State.ATTACK02() : [],
            State.ATTACK03() : [],
            State.TRANSFORM() : []
        }
        self.animations_Dark = {
            State.IDLE() : [],
            State.RUN() : [],
            State.JUMP() : [],
            State.FALL() : [],
            State.ATTACK01() : [],
            State.ATTACK02() : [],
            State.ATTACK03() : [],
            State.TRANSFORM() : []
        }
        self.animations = {
            PlayerType.LIGHT() : self.animations_Light,
            PlayerType.DARK() : self.animations_Dark
        }
        
        self.attack_states = [
            State.ATTACK01(),
            State.ATTACK02(),
            State.ATTACK03()
        ]
        
        for animation in self.animations_Light.keys():
            # print(animation.value)
            full_path = path_Light + animation
            self.animations_Light[animation] = readFolder(full_path)
        for animation in self.animations_Dark.keys():
            # print(animation.value)
            full_path = path_Dark + animation
            self.animations_Dark[animation] = readFolder(full_path)
    
    def animate(self):
        animation = self.animations[self.type][self.state]
        self.frame_idx += player_anim_speed[self.type][self.state]
        if self.frame_idx >= len(animation):
            self.frame_idx = 0
            if self.is_transforming:
                self.is_transforming = False
                if self.type == PlayerType.LIGHT():
                    self.type = PlayerType.DARK()
                    self.update_light(True)
                else:
                    self.type = PlayerType.LIGHT()
                    self.update_light(False)
                self.state = State.IDLE()
            if self.is_attacking:
                self.is_attacking = False
                self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        
        image = animation[int(self.frame_idx)]
        image = pg.transform.scale(image, (player_sizes[self.type][self.state][0] * player_scale, player_sizes[self.type][self.state][1] * player_scale))

        if self.facing_right:
            self.image = image
        else:
            flipped_image = pg.transform.flip(image, True, False)
            self.image = flipped_image
        
        if self.is_invincible:
            alpha = self.sin_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)
        
        if self.is_transforming:
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
        
        if self.is_transforming:
            return
        if self.is_attacking:
            return
        
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0 
            
        if self.direction.x != 0 and self.on_ground:
            self.SFX[SFXType.RUN()].unmute()
        else:
            self.SFX[SFXType.RUN()].mute()

        if keys[pg.K_x] and self.on_ground and not self.is_transforming:
            self.transform()
        if keys[pg.K_c] and not self.is_attacking and self.on_ground and not self.is_transforming:
            self.attack()
            self.direction.x = 0
        if keys[pg.K_SPACE]:
            if self.on_ground:
                self.jump()
            elif not self.get_peak:
                self.long_jump()
    
    def getState(self):
        if self.is_transforming:
            self.state = State.TRANSFORM()
        elif self.is_attacking:
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
        if self.is_transforming:
            return
        if self.is_attacking:
            return
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.SFX[SFXType.JUMP()].play()
        self.direction.y = self.jump_speed
    
    def long_jump(self):
        y_val = self.direction.y
        y_buff = self.jump_buffer
        y_val = y_val + y_buff
        if y_val < self.max_jump_speed:
            self.get_peak = True
            y_val = self.max_jump_speed
        self.direction.y = y_val

    def countdownAttackBuffer(self, delta_time):
        if self.attack_buffer_counter > 0:
            self.attack_buffer_counter -= delta_time
        else:
            self.attack_idx = 0
            self.attack_buffer_counter = self.attack_buffer
            
    def transform(self):
        self.particle.sprite.frame_idx = 0
        self.frame_idx = 0
        self.direction.x = 0
        self.is_transforming = True 
    
    def attack(self):
        self.SFX[SFXType.SWORD()].play()
        self.frame_idx = 0
        self.is_attacking = True
        self.direction.y = 0
        self.attack_buffer_counter = self.attack_buffer
        self.attack_idx += 1
        self.attack_idx %= len(self.attack_states)

    def get_damage(self):
        if not self.is_invincible:
            self.SFX[SFXType.HIT()].play()
            self.update_health(-10)
            self.is_invincible = True
            self.hurt_time = pg.time.get_ticks()

    def invincibility_timer(self):
        if self.is_invincible: 
            current_time = pg.time.get_ticks()
            if current_time - self.hurt_time >= self.invinciblity_duration:
                self.is_invincible = False
                
    def sin_value(self):
        value = sin(pg.time.get_ticks())
        if value >= 0 : return 255
        else: return 0
    
    def update(self, delta_time):
        self.countdownAttackBuffer(delta_time)
        self.gatherInput()
        self.getState()
        self.animate()
        self.invincibility_timer()
        self.sin_value()
        if self.is_transforming:
            self.particle.update(self.rect, self)
            self.particle.draw(self.display_surf)