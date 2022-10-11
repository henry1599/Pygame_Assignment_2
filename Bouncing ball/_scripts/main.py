from curses.panel import update_panels
import pygame, random, os, time
from pygame.locals import *
from Ball import *
from Constants import *
from helper import *
from player_management import *
from main_menu import *
from goal import *
from ingame_ui import *
# * START PRESET - DO NOT CHANGE
pygame.font.init()

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ground_surface = pg.image.load(BACKGROUND_PATH).convert()
ground_size = GetBackgroundScreenScale(BACKGROUND_WIDTH, BACKGROUND_HEIGHT, True)
ground_surface = pg.transform.scale(ground_surface, ground_size)
ground_position = (0, 0)

# * END PRESET
# * BALL DEMO
# * DO NOT ADD THIS INTO SPRITE GROUP
# * AS IT HAS ITS OWN UPDATE METHOD
random_speed = [-BALL_SPEED, BALL_SPEED]
# all_sprites = pygame.sprite.Group()
ball01 = Ball(
    screen = screen,
    image_path = BALL_PATH,
    position = (WIDTH / 2, HEIGHT / 2),
    scale = BALL_SIZE_IN_PIXEL,
    scale_multiplier = 0.3,
    anchor = Anchor.MID_CENTER,
    angle_delta_min = 1,
    angle_delta_max = 4,
    init_speed = (random_speed[random.randint(0, len(random_speed) - 1)], random_speed[random.randint(0, len(random_speed) - 1)]),
)
# * END BALL DEMO

ball_group = pygame.sprite.Group()
ball_group.add(ball01)
goal_left = Goal(
    screen = screen,
    image_path = GOAL_PATH,
    position = (-10, HEIGHT / 2),
    scale = (80, HEIGHT/3),
    scale_multiplier = 1,
    anchor = Anchor.MID_LEFT,
    angle_delta_min = 1,
    angle_delta_max = 4,
    bounceable_group = ball_group 
)
goal_right = Goal(
    screen = screen,
    image_path = GOAL_PATH,
    position = (WIDTH + 10, HEIGHT / 2),
    scale = (80, HEIGHT/3),
    scale_multiplier = 1,
    anchor = Anchor.MID_RIGHT,
    angle_delta_min = 1,
    angle_delta_max = 4,
    bounceable_group = ball_group 
)

# * ADD ALL OBJECTS ON SCREEN THAT CAN BE BOUNCED BY BALLS
bounceable_objects_group = pygame.sprite.Group()

main_menu = MainMenu(screen)
ingame_ui = InGameUI(screen)

default_player_position = [
    (WIDTH / 3, HEIGHT / 3),
    (WIDTH / 3, 2 * HEIGHT / 3),
    (2 * WIDTH / 3, HEIGHT / 3),
    (2 * WIDTH / 3, 2 * HEIGHT / 3)
]

def reset_position():
    for i in range(2):
        for j in range(2):
            players[i][j].reset(default_player_position[i * 2 + j])

    ball01.reset(
        (WIDTH / 2, HEIGHT / 2),
        (random_speed[random.randint(0, len(random_speed) - 1)], random_speed[random.randint(0, len(random_speed) - 1)])
    )

sep_line = pg.image.load(SEPARATED_LINE).convert_alpha()    
sep_line_rect = sep_line.get_rect(center = (WIDTH / 2, HEIGHT / 2))

win_sfx = pygame.mixer.Sound(COIN_WIN_SFX)
win_sfx.set_volume(COIN_WIN_VOLUME)

def main():
    running = True
    need_to_reset = False
    global players
    # * REMEMBER TO ASSIGN THIS LINE
    init_players(screen)
    for player in players:
        bounceable_objects_group.add(player)
    ball01.bounceable_group = bounceable_objects_group
    reset_position()
    
    pg.mixer.music.load(THEME)
    pg.mixer.music.set_volume(THEME_VOLUME)
    pg.mixer.music.play(-1)
    
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not main_menu.is_show:
                if event.key == pygame.K_f:
                    switch_players(TEAM_0)
                if event.key == pygame.K_h:
                    switch_players(TEAM_1)

        screen.blit(ground_surface, ground_position)
        if not main_menu.is_show:
            screen.blit(sep_line, sep_line_rect)
        
        if(main_menu.is_show):
            main_menu.update()
            pygame.display.flip()   
            continue

        is_player_2_goal = goal_left.update()
        is_player_1_goal = goal_right.update()

        ingame_ui.update(clock.get_time() / 1000, is_player_1_goal, is_player_2_goal)

        if (not ingame_ui.is_pause and not ingame_ui.is_end):
            if(need_to_reset):
                reset_position()
            need_to_reset = False 
            update_players(ball01, main_menu.is_multi)
            ball01.update()
        else:
            pg.mixer.Sound.play(win_sfx)
            need_to_reset = True

        ball01.draw()

        goal_left.draw()
        goal_right.draw()

        draw_players()
        
        ingame_ui.draw(not main_menu.is_multi)
        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()
