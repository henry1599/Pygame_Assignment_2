from enum import Enum

class GameState:
    @staticmethod 
    def OVERWORLD() : return 'overworld'
    @staticmethod
    def LEVEL() : return 'level'

class PlayerType:
    @staticmethod
    def LIGHT(): return 0 
    @staticmethod
    def DARK() : return 1

class VFX_State:
    @staticmethod
    def LIGHT2DARK() : return 'FX_lighttodark'
    @staticmethod
    def DARK2LIGHT() : return 'FX_darktolight'

class State:
    @staticmethod
    def IDLE(): return 'idle'
    @staticmethod
    def RUN(): return 'run'
    @staticmethod
    def JUMP(): return 'jump'
    @staticmethod
    def FALL(): return 'fall'
    @staticmethod
    def ATTACK01(): return 'attack1'
    @staticmethod
    def ATTACK02(): return 'attack2'
    @staticmethod
    def ATTACK03(): return 'attack3'
    @staticmethod
    def TRANSFORM(): return 'transform'
vertical_tile_number = 11
tile_size = 64
tile_real_size = 16
background_png_size = (6400, 704)

screen_height = vertical_tile_number * tile_size
screen_width = 1280

thunderstorm_color = (255, 255, 255, 255)


TERRAIN_TILESET_PATH = '../_levels/png/BWForest/Tileset.png'
TREE_AND_STUFF_PATH = '../_levels/png/BWForest/Trees_and_etc.png'
BACK_PATH = '../_levels/level_data/back_tree.png'
FRONT_PATH = '../_levels/level_data/front_tree.png'
BACKGROUND_PATH = '../_levels/level_data/background_gold.png'
COIN_PATH = '../_levels/png/coin01.png'
ICON_PATH = '../_assets/icon.png'


particle_scale = 2.5

particle_sizes_light2dark = (59, 88)
particle_sizes_dark2light = (71, 94)

particle_anim_speed_light2dark = 0.25
particle_anim_speed_dark2light = 0.25

particle_transform_sizes = {
    PlayerType.LIGHT() : particle_sizes_light2dark,
    PlayerType.DARK() : particle_sizes_dark2light
}
particle_anim_transform_speed = {
    PlayerType.LIGHT() : particle_anim_speed_light2dark,
    PlayerType.DARK() : particle_anim_speed_dark2light
}

player_scale = 2.5
player_sizes_light = {
    State.IDLE() : (15, 18),
    State.RUN() : (19, 21),
    State.JUMP() : (13, 25),
    State.FALL() : (16, 30),
    State.ATTACK01() : (52, 27),
    State.ATTACK02() : (52, 27),
    State.ATTACK03() : (52, 27),
    State.TRANSFORM() : (23, 60)
}
player_anim_speed_light = {
    State.IDLE() : 0.15,
    State.RUN(): 0.3,
    State.JUMP() : 0.15,
    State.FALL() : 0.15,
    State.ATTACK01() : 0.3,
    State.ATTACK02() : 0.25,
    State.ATTACK03() : 0.25,
    State.TRANSFORM() : 0.25
}
player_sizes_dark = {
    State.IDLE() : (22, 18),
    State.RUN() : (26, 22),
    State.JUMP() : (21, 27),
    State.FALL() : (18, 37),
    State.ATTACK01() : (65, 27),
    State.ATTACK02() : (65, 27),
    State.ATTACK03() : (65, 27),
    State.TRANSFORM() : (26, 65)
}
player_anim_speed_dark = {
    State.IDLE() : 0.15,
    State.RUN(): 0.3,
    State.JUMP() : 0.15,
    State.FALL() : 0.15,
    State.ATTACK01() : 0.3,
    State.ATTACK02() : 0.25,
    State.ATTACK03() : 0.25,
    State.TRANSFORM() : 0.25
}
player_sizes = {
    PlayerType.LIGHT() : player_sizes_light,
    PlayerType.DARK() : player_sizes_dark
}
player_anim_speed = {
    PlayerType.LIGHT() : player_anim_speed_light,
    PlayerType.DARK() : player_anim_speed_dark
}

level_theme_light = {
    'tile' : 'grey',
    'background' : 'black'
}
level_theme_dark = {
    'tile' : 'black',
    'background' : 'grey'
}
level_theme = {
    PlayerType.LIGHT() : level_theme_light,
    PlayerType.DARK() : level_theme_dark
}