import pygame
from components import *
from Constants import *

class ButtonTextRenderer(TextRenderer):
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
        border_radius = 2,
        type = ButtonType.START
    ):
        super().__init__(screen, font_path, position, string, size, fcolor, anchor, is_outline, ocolor, border_radius)
        self.clicked = False
        self.type = type
    
    def gather_input(self, start_action):
        if not self.clicked:
            mouse_presses = pg.mouse.get_pressed()
            if mouse_presses[0]:
                if self.rect.collidepoint(pg.mouse.get_pos()):
                    self.clicked = True
                    if self.type == ButtonType.START:
                        start_action()
                        
        # pass
    
    def update(self):
        super().update()
            
    def draw_text(self):
        super().draw_text()
    
    def draw_text_support(self, font_path, position, string, size, fcolor, anchor, window):
        super().draw_text_support(font_path, position, string, size, fcolor, anchor, window)

    def draw_text_with_outline(self):
        super().draw_text_with_outline()


class MainMenu():
    def __init__(self, screen):
        self.is_show = True
        self.is_multi = True
        self.game_name_text = TextRenderer(
            screen,
            FONT_PATH, 
            (WIDTH / 2, 100), 
            GAME_NAME, 
            GAME_NAME_TEXT_SIZE, 
            GAME_NAME_COLOR, 
            Anchor.MID_CENTER,
            True,
            GAME_NAME_COLOR_OUTLINE, 
            4
        )
        self.single_player = ButtonTextRenderer(
            screen,
            FONT_PATH, 
            (WIDTH / 2 - 100, HEIGHT / 2), 
            SINGLE_TITLE, 
            TITLE_TEXT_SIZE, 
            TITLE_COLOR, 
            Anchor.MID_CENTER,
            True,
            GAME_NAME_COLOR_OUTLINE, 
            2,
            ButtonType.START
        )
        self.multi_player = ButtonTextRenderer(
            screen,
            FONT_PATH, 
            (WIDTH / 2 + 100, HEIGHT / 2), 
            MULTIPLE_TITLE, 
            TITLE_TEXT_SIZE, 
            TITLE_COLOR, 
            Anchor.MID_CENTER,
            True,
            GAME_NAME_COLOR_OUTLINE, 
            2,
            ButtonType.START
        )
    def start_single(self):
        self.is_show = False
        self.is_multi = False
    def start_multi(self):
        self.is_show = False
        self.is_multi = True
    def quit(self):
        pass
    def update(self):
        self.game_name_text.update()
        self.single_player.update()
        self.multi_player.update()
        self.single_player.gather_input(self.start_single)
        self.multi_player.gather_input(self.start_multi)