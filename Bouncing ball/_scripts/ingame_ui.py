from Constants import *
from components import *
import math

class InGameUI():
    def __init__(self,screen):
        self.is_pause = False
        self.is_end = False
        self.waiting_time = 0
        self.timer = TIME_PER_MATCH
        self.player_1_score = 0
        self.player_2_score = 0
        self.last_player_goal = 0
        self.timer_ui = TextRenderer(
            screen=screen,
            font_path=FONT_PATH,
            position=(WIDTH/2, 0),
            string="60",
            size=TITLE_TEXT_SIZE, 
            fcolor=TITLE_COLOR, 
            anchor=Anchor.TOP_CENTER
        )
        self.player01_instruction_movement = TextRenderer(
            screen=screen,
            font_path=FONT_PATH,
            position=(10,10),
            string="W,A,S,D for movement",
            size=20,
            fcolor=TITLE_COLOR,
            anchor=Anchor.TOP_LEFT
        )
        self.player01_instruction_switch = TextRenderer(
            screen=screen,
            font_path=FONT_PATH,
            position=(10,30),
            string="F to switch",
            size=20,
            fcolor=TITLE_COLOR,
            anchor=Anchor.TOP_LEFT
        )
        self.player02_instruction_movement = TextRenderer(
            screen=screen,
            font_path=FONT_PATH,
            position=(WIDTH-10,10),
            string="I,J,K,L for movement",
            size=20,
            fcolor=TITLE_COLOR,
            anchor=Anchor.TOP_RIGHT
        )
        self.player02_instruction_switch = TextRenderer(
            screen=screen,
            font_path=FONT_PATH,
            position=(WIDTH-10,30),
            string="H to switch",
            size=20,
            fcolor=TITLE_COLOR,
            anchor=Anchor.TOP_RIGHT
        )
        self.player_1_score_ui = TextRenderer(
            screen=screen,
            font_path=FONT_PATH,
            position=(WIDTH/2 - 100, 0),
            string="0",
            size=TITLE_TEXT_SIZE, 
            fcolor=TITLE_COLOR, 
            anchor=Anchor.TOP_CENTER
        )
        self.player_2_score_ui = TextRenderer(
            screen=screen,
            font_path=FONT_PATH,
            position=(WIDTH/2 + 100, 0),
            string="0",
            size=TITLE_TEXT_SIZE, 
            fcolor=TITLE_COLOR, 
            anchor=Anchor.TOP_CENTER
        )
        self.fade_screen = SpriteRenderer(
            screen=screen,
            image_path=FADE_IMAGE_PATH,
            position=(WIDTH/2, HEIGHT/2),
            scale=(WIDTH, HEIGHT),
            scale_multiplier=1,
            anchor=Anchor.MID_CENTER,
        )
        self.annoucement = TextRenderer(
            screen=screen,
            font_path=FONT_PATH,
            position=(WIDTH/2, HEIGHT/2),
            string="",
            size=TITLE_TEXT_SIZE, 
            fcolor=TITLE_COLOR, 
            anchor=Anchor.MID_CENTER,
            is_outline=True,
            ocolor=GAME_NAME_COLOR_OUTLINE
        )

    def update(self, delta_time, player_1_goal, player_2_goal):
        if(player_1_goal and not self.is_pause and not self.is_end):
            self.is_pause = True
            self.player_1_score += 1
            self.player_1_score_ui.text = str(self.player_1_score)
            self.last_player_goal = 1
            self.waiting_time = 2
            
        if(player_2_goal and not self.is_pause and not self.is_end):
            self.is_pause = True
            self.player_2_score += 1
            self.player_2_score_ui.text = str(self.player_2_score)
            self.last_player_goal = 2
            self.waiting_time = 2

        if(not self.is_pause and not self.is_end):    
            self.last_player_goal = 0
            self.timer = self.timer - delta_time
            self.timer_ui.text = str(math.ceil(self.timer))
        else:
            self.waiting_time = self.waiting_time - delta_time
            if(self.waiting_time <= 0):
                self.is_pause = False

    def draw(self, is_multi):
        self.timer_ui.update()
        self.player_1_score_ui.update()
        self.player_2_score_ui.update()
        self.player01_instruction_movement.update()
        self.player01_instruction_switch.update()
        if not is_multi:
            self.player02_instruction_movement.update()
            self.player02_instruction_switch.update()
        if(self.last_player_goal):
            self.fade_screen.draw()
            self.annoucement.text = "Player " + str(self.last_player_goal) + " goal !!!"
            self.annoucement.update()
            pass
        if(self.timer <= 0):
            self.is_end = True
            self.fade_screen.draw()
            if(self.player_1_score > self.player_2_score):
                player_win = "Player 1 win !!!"
            elif(self.player_1_score < self.player_2_score):
                player_win = "Player 2 win !!!"
            else:
                player_win = "Draw !!!"
            self.annoucement.text = player_win
            self.annoucement.update()
