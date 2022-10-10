from curses.panel import update_panels
import pygame, random, os, time
from pygame.locals import *
from Ball import *
from Constants import *
from helper import *
from player_management import *

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
random_speed = [-10, 10]
# all_sprites = pygame.sprite.Group()
ball01 = Ball(
    screen = screen,
    image_path = BALL_PATH,
    position = (WIDTH / 2, HEIGHT / 2),
    scale = BALL_SIZE_IN_PIXEL,
    scale_multiplier = 0.1,
    anchor = Anchor.MID_CENTER,
    angle_delta_min = 1,
    angle_delta_max = 4,
    init_speed = (random_speed[random.randint(0, len(random_speed) - 1)], random_speed[random.randint(0, len(random_speed) - 1)]),
)
# * END BALL DEMO


# * ADD ALL OBJECTS ON SCREEN THAT CAN BE BOUNCED BY BALLS
bounceable_objects_group = pygame.sprite.Group()
# bounceable_objects_group.add(test_obj01)
# bounceable_objects_group.add(test_obj02)
# bounceable_objects_group.add(test_obj03)
# bounceable_objects_group.add(test_obj04)

def main(multiplayer):
    running = True
    global players
    init_players(screen)
    for player in players:
        bounceable_objects_group.add(player)
    ball01.bounceable_group = bounceable_objects_group
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    switch_players(TEAM_0)
                if event.key == pygame.K_h:
                    switch_players(TEAM_1)
                
        update_players(ball01, multiplayer)
        # if ball.is_into_hold == True:
        #     print('Lose')
        
        ball01.update()
        # test_obj01.update()
        # test_obj02.update()
        # test_obj03.update()
        # test_obj04.update()

        screen.blit(ground_surface, ground_position)
        ball01.draw()
        draw_players()
        
        # test_obj01.draw()
        # test_obj02.draw()
        # test_obj03.draw()
        # test_obj04.draw()
        # if ball.is_into_hold == True:
        #     running = False
        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main(False)
