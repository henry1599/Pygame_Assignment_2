import pygame, random, os, time
from enum import Enum

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
WIDTH  = 800
HEIGHT = 450
FPS = 60
random_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

BALL_PATH = '../_assets/sprites/balls/ball.png'
BALL_SIZE_IN_PIXEL = (500, 500)

BACKGROUND_PATH = '../_assets/sprites/backgrounds/Background.png'
BACKGROUND_WIDTH = 1300
BACKGROUND_HEIGHT = 866

PLAYER_TEST_PATH = '../_assets/sprites/players/Test/player_test.png'
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