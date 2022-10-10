import numpy as np
from player import *
from pygame.locals import *

TEAM_0 = 0
TEAM_1 = 1
PLAYER_0 = 0
PLAYER_1 = 1

KEYBOARD_0 = {"left": pygame.K_a, "right": pygame.K_d, "up": pygame.K_w, "down": pygame.K_s, "switch": pygame.K_f}
KEYBOARD_1 = {"left": pygame.K_j, "right": pygame.K_l, "up": pygame.K_i, "down": pygame.K_k, "switch": pygame.K_h}

players = [[],[]]
focus_player = [0, 0]

player_pos = [
    [(WIDTH / 4, HEIGHT / 4), (WIDTH / 4, 3 * HEIGHT / 4)],
    [(3 * WIDTH / 4, HEIGHT / 4), (3 * WIDTH / 4, 3 * HEIGHT / 4)]
]

def init_players(screen):
    for i in range(2):
        for j in range(2):
            player = Player(
            screen = screen,
            image_path = PLAYER_TEST_PATH,
            position = player_pos[i][j],
            speed = 3.0,
            scale = PLAYER_TEST_SIZE,
            scale_multiplier = 0.3,
            anchor = Anchor.MID_CENTER,
            angle_delta_min = 1,
            angle_delta_max = 4)
            players[i].append(player)

def update_players(ball, multiplayer):
    keys = pygame.key.get_pressed()
    if not keys:
        return
    global current_player
    if keys[KEYBOARD_0["left"]] or keys[KEYBOARD_0["right"]] or keys[KEYBOARD_0["up"]] or keys[KEYBOARD_0["down"]]:
        moverment(players[TEAM_0][focus_player[TEAM_0]], KEYBOARD_0)

    if multiplayer:
        if keys[KEYBOARD_1["left"]] or keys[KEYBOARD_1["right"]] or keys[KEYBOARD_1["up"]] or keys[KEYBOARD_1["down"]]:
            moverment(players[TEAM_1][focus_player[TEAM_1]], KEYBOARD_1)
    else:
        updateBot(ball)

    if keys[KEYBOARD_1["left"]] or keys[KEYBOARD_1["right"]] or keys[KEYBOARD_1["up"]] or keys[KEYBOARD_1["down"]]:
        moverment(players[TEAM_1][focus_player[TEAM_1]], KEYBOARD_1)

    
    
def draw_players():
    for team in players:
        for player in team:
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

def switch_players(team):
    focus_player[team] = int(not(focus_player[team]))

def get_all_players():
    return players

time_focus_bot = 0
dir = [0, 0]

def updateBot(ball):
    dir = [0,0]
    # global time_focus_bot
    # each 2s, update new bot's player to focus 
    # if time_focus_bot == 0:
    if get_distance_to_ball(ball, players[TEAM_1][0]) >= get_distance_to_ball(ball, players[TEAM_1][1]):
        focus_player[TEAM_1] = 0
    else:
        focus_player[TEAM_1] = 1
    #         time_focus_bot = FPS * 2
    # time_focus_bot -= 1
    player = players[TEAM_1][focus_player[TEAM_1]]
    
    # each 0.5s, update new velocity of bot's player
    # if time_focus_bot % (FPS / 2) == 0:
    delta_x = ball.rect.x - player.position[0]
    delta_y = ball.rect.y - player.position[1]
    if abs(delta_y) >= abs(delta_x):
        if delta_y > 0: dir[1] = 1
        else: dir[1] = -1
    else:
        if delta_x > 0: dir[0] = 1
        else: dir[0] = -1

    player.moverment(dir)


def get_distance_to_ball(ball, player):
    return abs(ball.rect.x - player.position[0]) + abs(ball.rect.y - player.position[1])
