import pygame, random, os, time
from enum import Enum

PLAYER_SPEED = 3.0
BALL_SPEED = 3.0

COLLIDE_INFO = {
    'BL' : ['botton', 'left'],
    'BLR' : ['bottom', 'left', 'right'],
    'BR' : ['bottom', 'right'],
    'BRT' : ['bottom', 'right', 'top'],
    'TR' : ['top','right'],
    'TLR' : ['top', 'left', 'right'],
    'TL' : ['top', 'left'],
    'BTL' : ['bottom', 'top', 'left']
}

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue =(0,0,255)
WIDTH  = 1280
HEIGHT = 720
FPS = 60
random_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

BALL_PATH = '../_assets/Casino/Casino_Coin.png'
BALL_SIZE_IN_PIXEL = (182, 182)

SEPARATED_LINE = '../_assets/Casino/Separated_Line.png'

BACKGROUND_PATH = '../_assets/Casino/Casino_Table.png'
BACKGROUND_WIDTH = 1676
BACKGROUND_HEIGHT = 1119

PLAYER_RED_01 = '../_assets/Casino/Player_Red_01.png'
PLAYER_RED_02 = '../_assets/Casino/Player_Red_02.png'
PLAYER_BLACK_01 = '../_assets/Casino/Player_Black_01.png'
PLAYER_BLACK_02 = '../_assets/Casino/Player_Black_02.png'

PLAYER_SPRITES = [
    PLAYER_RED_01,
    PLAYER_RED_02,
    PLAYER_BLACK_01,
    PLAYER_BLACK_02
]

GOAL_PATH = '../_assets/sprites/players/Test/player_test.png'

PLAYER_TEST_SIZE = (270, 270)

class Direction(Enum):
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3

DIRECTION = {
    Direction.UP : "up",
    Direction.DOWN : "down",
    Direction.LEFT : "left",
    Direction.RIGHT : "right",
}

class ButtonType(Enum):
    START = 0,

class Scene(Enum):
    MAIN_MENU = 0,
    HISTORY = 1,
    GAMEPLAY = 2,

FONT_PATH  = '../_fonts/Dosis/Dosis-Bold.ttf'

GAME_NAME = "BOUNCING GAME"
GAME_NAME_TEXT_SIZE = 100
GAME_NAME_COLOR = (255, 255, 255)
GAME_NAME_COLOR_OUTLINE = (0, 0, 0)

SINGLE_TITLE = "PvE"
MULTIPLE_TITLE = "PvP"
TITLE_TEXT_SIZE = 50
TITLE_COLOR = (255, 255, 255)

FADE_IMAGE_PATH = '../_assets/sprites/fade/Fade.png'

TIME_PER_MATCH = 60