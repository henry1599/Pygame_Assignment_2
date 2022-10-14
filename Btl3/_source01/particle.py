import pygame as pg
from helper import *
from setting import *

class VFX_Transform(pg.sprite.Sprite):
    def __init__(self, position, init_type, player):
        super().__init__()
        self.getAssets()
        self.frame_idx = 0
        self.image = self.animations[init_type][self.frame_idx]
        self.image = pg.transform.scale(self.image, (particle_sizes_light2dark[0] * particle_scale, particle_sizes_light2dark[1] * particle_scale))
        self.rect = self.image.get_rect(center = position)
        self.type = init_type
        self.player = player
    
    def setPosition(self, position):
        self.rect.center = position.center
    
    def getAssets(self):
        path_Light = '../_assets/Character/'
        path_Dark = '../_assets/Dark/Dark/'
        self.fromVFX2PlayerType = {
            VFX_State.LIGHT2DARK() : PlayerType.LIGHT(),
            VFX_State.DARK2LIGHT() : PlayerType.DARK(),
        }
        self.animations = {
            PlayerType.LIGHT() : [],
            PlayerType.DARK() : []
        }
        
        full_path = path_Light + VFX_State.LIGHT2DARK()
        self.animations[PlayerType.LIGHT()] = readFolder(full_path)
        full_path = path_Dark + VFX_State.DARK2LIGHT()
        self.animations[PlayerType.DARK()] = readFolder(full_path)
    
    def animate(self):
        animation = self.animations[self.type]
        
        self.frame_idx += particle_anim_transform_speed[self.player.type]
        if self.frame_idx >= len(animation):
            self.frame_idx = 0
        
        image = animation[int(self.frame_idx)]
        image = pg.transform.scale(image, (particle_transform_sizes[self.player.type][0] * particle_scale, particle_transform_sizes[self.player.type][1] * particle_scale))

        if self.player.facing_right:
            self.image = image
        else:
            flipped_image = pg.transform.flip(image, True, False)
            self.image = flipped_image
    
    def update(self, rect, player):
        self.player = player
        self.type = player.type
        self.setPosition(rect)
        self.animate()