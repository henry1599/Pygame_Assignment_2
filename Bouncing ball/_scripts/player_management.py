import numpy as np
from player import *
from pygame.locals import *

TEAM_0 = 0
TEAM_1 = 1
PLAYER_0 = 0
PLAYER_1 = 1

KEYBOARD_0 = {"left": pygame.K_a, "right": pygame.K_d, "up": pygame.K_w, "down": pygame.K_s}
KEYBOARD_1 = {"left": pygame.K_j, "right": pygame.K_l, "up": pygame.K_i, "down": pygame.K_k}

players = [[],[]]
focus_player = [0, 0]

def init_players(screen):
    for i in range(2):
        for j in range(2):
            player = Player(
            screen = screen,
            image_path = PLAYER_TEST_PATH,
            position = (WIDTH / 3, HEIGHT / 3),
            speed = 3.0,
            scale = PLAYER_TEST_SIZE,
            scale_multiplier = 0.3,
            anchor = Anchor.MID_CENTER,
            angle_delta_min = 1,
            angle_delta_max = 4)
            players[i].append(player)

def update_players():
    keys = pygame.key.get_pressed()
    global current_player
    if keys[KEYBOARD_0["left"]] or keys[KEYBOARD_0["right"]] or keys[KEYBOARD_0["up"]] or keys[KEYBOARD_0["down"]]:
        moverment(players[TEAM_0][focus_player[TEAM_0]], KEYBOARD_0)
        # print(players[TEAM_0][PLAYER_0].position, players[TEAM_0][PLAYER_1].position, players[TEAM_1][PLAYER_0].position, players[TEAM_1][PLAYER_1].position)
    if keys[KEYBOARD_1["left"]] or keys[KEYBOARD_1["right"]] or keys[KEYBOARD_1["up"]] or keys[KEYBOARD_1["down"]]:
        moverment(players[TEAM_1][focus_player[TEAM_1]], KEYBOARD_1)
        # print(players[TEAM_0][PLAYER_0].position, players[TEAM_0][PLAYER_1].position, players[TEAM_1][PLAYER_0].position, players[TEAM_1][PLAYER_1].position)
    
def draw_players():
    for team in players:
        for player in team:
            print(players[TEAM_0][PLAYER_0].position, players[TEAM_0][PLAYER_1].position, players[TEAM_1][PLAYER_0].position, players[TEAM_1][PLAYER_1].position)
            player.draw()
        

def moverment(player, keyboard):
    keys = pygame.key.get_pressed()
    dir_x, dir_y = 0, 0
    if keys[keyboard["left"]]:
        dir_x -= 1
    elif keys[keyboard["right"]]:
        dir_x += 1
    if keys[keyboard["up"]]:
        dir_y -= 1
    elif keys[keyboard["down"]]:
        dir_y += 1
    player.moverment((dir_x, dir_y))
