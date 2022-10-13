from enum import Enum

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
level_map = [
'                            ',
'                            ',
'                            ',
' X     XXX            XX    ',
' XX P                       ',
' XXXX         XX         XX ',
' XXXX       XX              ',
' XX    X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

tile_size = 64
player_scale = 2.5
player_sizes = {
    State.IDLE() : (15, 18),
    State.RUN() : (19, 21),
    State.JUMP() : (13, 25),
    State.FALL() : (16, 30),
    State.ATTACK01() : (52, 27),
    State.ATTACK02() : (52, 27),
    State.ATTACK03() : (52, 27)
}
player_anim_speed = {
    State.IDLE() : 0.15,
    State.RUN(): 0.3,
    State.JUMP() : 0.15,
    State.FALL() : 0.15,
    State.ATTACK01() : 0.3,
    State.ATTACK02() : 0.25,
    State.ATTACK03() : 0.25
}
screen_width = 1200
screen_height = len(level_map) * tile_size