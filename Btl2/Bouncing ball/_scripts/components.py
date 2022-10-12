from enum import Enum
import pygame as pg
import random
class Anchor(Enum):
    TOP_LEFT = 0, 
    MID_LEFT = 1,
    BOTTOM_LEFT = 2, 
    TOP_CENTER = 3,
    MID_CENTER = 4,      
    BOTTOM_CENTER = 5, 
    TOP_RIGHT = 6,
    MID_RIGHT = 7,
    BOTTOM_RIGHT = 8

ROTATE_FACTOR = [-1, 1]
class SpriteRenderer (pg.sprite.Sprite):
    def __init__(self, 
                 # * Screen to draw on
                 screen,
                 # * Image path
                 image_path : str, 
                 # * Init position
                 position : tuple = (0, 0), 
                 # * Actual size of image (in pixel)
                 scale : tuple = (1, 1), 
                 # * How much will this image be scaled
                 scale_multiplier : float = 1, 
                 # * Anchor to position
                 anchor : Anchor = Anchor.TOP_LEFT,
                 # * Angle used for rotate image
                 angle_delta_min = 1,
                 angle_delta_max = 4):
        super().__init__()
        self.screen = screen
        self.base_scale = scale 
        self.scale_multiplier = scale_multiplier
        self.scale = (self.base_scale[0] * scale_multiplier, self.base_scale[1] * self.scale_multiplier)
        self.image = pg.image.load(image_path).convert_alpha()
        self.position = position
        self.ScaleImage(self.base_scale, self.scale_multiplier)
        if anchor == Anchor.TOP_LEFT:
            self.rect = self.image.get_rect(topleft = position)
        elif anchor == Anchor.MID_LEFT:
            self.rect = self.image.get_rect(midleft = position)
        elif anchor == Anchor.BOTTOM_LEFT:
            self.rect = self.image.get_rect(bottomleft = position)
        elif anchor == Anchor.TOP_CENTER:
            self.rect = self.image.get_rect(midtop = position)
        elif anchor == Anchor.MID_CENTER:
            self.rect = self.image.get_rect(center = position)
        elif anchor == Anchor.BOTTOM_CENTER:
            self.rect = self.image.get_rect(midbottom = position)
        elif anchor == Anchor.TOP_RIGHT:
            self.rect = self.image.get_rect(topright = position)
        elif anchor == Anchor.MID_RIGHT:
            self.rect = self.image.get_rect(midright = position)
        elif anchor == Anchor.BOTTOM_RIGHT:
            self.rect = self.image.get_rect(bottomright = position)
        self.angle = 0
        self.angle_delta = random.uniform(angle_delta_min, angle_delta_max)
        self.rotate_factor = ROTATE_FACTOR[random.randint(0, 1)]
        self.image_copy = pg.transform.rotate(self.image, self.angle).convert_alpha()
    def GatherInput(self):
        pass
    
    def ScaleImage(self, base_scale : tuple, scale_multiplier : float):
        self.image = pg.transform.scale(self.image, (base_scale[0] * scale_multiplier, base_scale[1] * scale_multiplier))
    
    def ApplyGravity(self):
        pass
    
    def PlayerAnimation(self):
        pass
    
    def update(self):
        self.angle += self.angle_delta * self.rotate_factor
        self.image_copy = pg.transform.rotate(self.image, self.angle)

    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    def draw_with_rotation(self):
        self.screen.blit(self.image_copy, (self.position[0] - int(self.image_copy.get_width() / 2), self.position[1] - int(self.image_copy.get_height() / 2)))

class TextRenderer(pg.font.Font):
    def __init__(
        self,
        screen,
        font_path, 
        position, 
        string, 
        size, 
        fcolor, 
        anchor,
        is_outline = False,
        ocolor = (255, 255, 255),
        border_radius = 2
    ):
        super().__init__(font_path, size)
        self.screen = screen
        self.font_path = font_path
        self.font = pg.font.Font(font_path, size)
        self.position = position
        self.text = string
        self.size = size 
        self.font_color = fcolor
        self.outline_color = ocolor
        self.border_radius = border_radius
        self.is_outline = is_outline 
        self.anchor = anchor
        self.render = self.font.render(self.text, True, self.font_color)
        self.rect = self.render.get_rect()
        if self.anchor == Anchor.TOP_LEFT:
            self.rect.topleft = self.position
        elif self.anchor == Anchor.MID_LEFT:
            self.rect.midleft = self.position
        elif self.anchor == Anchor.BOTTOM_LEFT:
            self.rect.bottomleft = self.position
        elif self.anchor == Anchor.TOP_CENTER:
            self.rect.midtop = self.position
        elif self.anchor == Anchor.MID_CENTER:
            self.rect.center = self.position
        elif self.anchor == Anchor.BOTTOM_CENTER:
            self.rect.midbottom = self.position
        elif self.anchor == Anchor.TOP_RIGHT:
            self.rect.topright = self.position
        elif self.anchor == Anchor.MID_RIGHT:
            self.rect.midright = self.position
        elif self.anchor == Anchor.BOTTOM_RIGHT:
            self.rect.bottomright = self.position
        
    
    def GatherInput(self):
        pass
    
    def update(self):
        self.GatherInput()
        if self.is_outline:
            self.draw_text_with_outline()
        else:
            self.draw_text()
            
    def draw_text(self):
        text = self.font.render(self.text, True, self.font_color)
        self.screen.blit(text, self.rect)
    
    def draw_text_support(self, font_path, position, string, size, fcolor, anchor, window):
        font = pg.font.Font(font_path, size)
        text = font.render(string, True, fcolor)
        textbox = text.get_rect()
        if anchor == Anchor.TOP_LEFT:
            textbox.topleft = position
        elif anchor == Anchor.MID_LEFT:
            textbox.midleft = position
        elif anchor == Anchor.BOTTOM_LEFT:
            textbox.bottomleft = position
        elif anchor == Anchor.TOP_CENTER:
            textbox.midtop = position
        elif anchor == Anchor.MID_CENTER:
            textbox.center = position
        elif anchor == Anchor.BOTTOM_CENTER:
            textbox.midbottom = position
        elif anchor == Anchor.TOP_RIGHT:
            textbox.topright = position
        elif anchor == Anchor.MID_RIGHT:
            textbox.midright = position
        elif anchor == Anchor.BOTTOM_RIGHT:
            textbox.bottomright = position
        window.blit(text, textbox)

    def draw_text_with_outline(self):
        self.draw_text_support(self.font_path, (self.position[0] + self.border_radius, self.position[1] - self.border_radius) , self.text, self.size, self.outline_color, self.anchor, self.screen)
        self.draw_text_support(self.font_path, (self.position[0] + self.border_radius, self.position[1] - self.border_radius) , self.text, self.size, self.outline_color, self.anchor, self.screen)
        self.draw_text_support(self.font_path, (self.position[0] - self.border_radius, self.position[1] + self.border_radius) , self.text, self.size, self.outline_color, self.anchor, self.screen)
        self.draw_text_support(self.font_path, (self.position[0] - self.border_radius, self.position[1] + self.border_radius) , self.text, self.size, self.outline_color, self.anchor, self.screen) 
        self.draw_text_support(self.font_path, (self.position[0] + self.border_radius, self.position[1] + self.border_radius) , self.text, self.size, self.outline_color, self.anchor, self.screen)
        self.draw_text_support(self.font_path, (self.position[0] - self.border_radius, self.position[1] - self.border_radius) , self.text, self.size, self.outline_color, self.anchor, self.screen) 
        self.draw_text_support(self.font_path, (self.position[0], self.position[1]), self.text, self.size, self.font_color, self.anchor, self.screen)