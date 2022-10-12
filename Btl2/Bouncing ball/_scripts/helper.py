from Constants import *
import pygame as pg
from components import *

# * Used to scale an background image full screen
# * param :
# * _bg_width, _bg_height : Actual size of the image (in pixel)
# * _scale_by_width : Full image width with screen width if true (height if false)
def GetBackgroundScreenScale(_bg_width, _bg_height, _scale_by_width = False):
    background_width_ratio = WIDTH / _bg_width
    background_height_ratio = HEIGHT / _bg_height
    background_ratio = 1.0
    if _scale_by_width:
        background_ratio = background_width_ratio
    else:
        background_ratio = background_height_ratio
    return (background_ratio * _bg_width, background_ratio * _bg_height)


# * Draw a text
def draw_text(font_path, position, string, size, fcolor, anchor, window):
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

# * draw a text with outline
def draw_text_with_outline(font_path, position, string, size, fcolor, ocolor, border_radius, anchor, window):
    draw_text(font_path, (position[0] + border_radius, position[1] - border_radius) , string, size, ocolor, anchor, window)
    draw_text(font_path, (position[0] + border_radius, position[1] - border_radius) , string, size, ocolor, anchor, window)
    draw_text(font_path, (position[0] - border_radius, position[1] + border_radius) , string, size, ocolor, anchor, window)
    draw_text(font_path, (position[0] - border_radius, position[1] + border_radius) , string, size, ocolor, anchor, window) 
    draw_text(font_path, (position[0] + border_radius, position[1] + border_radius) , string, size, ocolor, anchor, window)
    draw_text(font_path, (position[0] - border_radius, position[1] - border_radius) , string, size, ocolor, anchor, window) 
    draw_text(font_path, (position[0], position[1]), string, size, fcolor, anchor, window)

    