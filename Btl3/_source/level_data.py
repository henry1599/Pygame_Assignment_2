from setting import *

class LevelProperties:
    @staticmethod
    def NODE_POS() : return 'node_pos'
    @staticmethod
    def CONTENT() : return 'content'
    @staticmethod
    def UNLOCK() : return 'unlock'
    @staticmethod
    def NODE_PNG() : return 'node_png'
    @staticmethod
    def NODE_LOCK() : return 'node_lock'

class LevelType:
    @staticmethod
    def NOTHING() : return -1
    @staticmethod
    def TERRAIN() : return 0
    @staticmethod
    def PLAYER() : return 1
    @staticmethod
    def FRONT() : return 2
    @staticmethod
    def ENEMY() : return 3
    @staticmethod
    def CONSTRAINTS() : return 4
    @staticmethod
    def COLLECTIBLE() : return 5
    @staticmethod
    def BACKGROUND_01() : return 6
    @staticmethod
    def BACKGROUND_02() : return 7
    @staticmethod
    def BACKGROUND_03() : return 8
    @staticmethod
    def BACKGROUND_04() : return 9
    @staticmethod
    def BACKGROUND_05() : return 10
    @staticmethod
    def BACKGROUND_06() : return 11
    @staticmethod
    def BACK() : return 12

level_0 = {
    LevelType.TERRAIN() : '../_levels/0/level_0_16x16._terrain.csv',
    LevelType.PLAYER() : '../_levels/0/level_0_16x16._player_title.csv',
    LevelType.FRONT() : '../_levels/0/level_0_16x16._front_tree.csv',
    LevelType.ENEMY() : '../_levels/0/level_0_16x16._enemy.csv',
    LevelType.CONSTRAINTS() : '../_levels/0/level_0_16x16._constraints.csv',
    LevelType.COLLECTIBLE() : '../_levels/0/level_0_16x16._collectible.csv',
    LevelType.BACKGROUND_06() : '../_levels/0/level_0_16x16._background_06.csv',
    LevelType.BACKGROUND_05() : '../_levels/0/level_0_16x16._background_05.csv',
    LevelType.BACKGROUND_04() : '../_levels/0/level_0_16x16._background_04.csv',
    LevelType.BACKGROUND_03() : '../_levels/0/level_0_16x16._background_03.csv',
    LevelType.BACKGROUND_02() : '../_levels/0/level_0_16x16._background_02.csv',
    LevelType.BACKGROUND_01() : '../_levels/0/level_0_16x16._background_01.csv',
    LevelType.BACK() : '../_levels/0/level_0_16x16._back_tree.csv',
    LevelProperties.NODE_POS() : (200, screen_height / 2),
    LevelProperties.UNLOCK() : 1,
    LevelProperties.NODE_PNG() : '../_assets/overworld/Level01.png',
    LevelProperties.NODE_LOCK() : '../_assets/overworld/LevelLocl.png'
}
level_1 = {
    LevelType.TERRAIN() : '../_levels/0/level_0_16x16._terrain.csv',
    LevelType.PLAYER() : '../_levels/0/level_0_16x16._player_title.csv',
    LevelType.FRONT() : '../_levels/0/level_0_16x16._front_tree.csv',
    LevelType.ENEMY() : '../_levels/0/level_0_16x16._enemy.csv',
    LevelType.CONSTRAINTS() : '../_levels/0/level_0_16x16._constraints.csv',
    LevelType.COLLECTIBLE() : '../_levels/0/level_0_16x16._collectible.csv',
    LevelType.BACKGROUND_06() : '../_levels/0/level_0_16x16._background_06.csv',
    LevelType.BACKGROUND_05() : '../_levels/0/level_0_16x16._background_05.csv',
    LevelType.BACKGROUND_04() : '../_levels/0/level_0_16x16._background_04.csv',
    LevelType.BACKGROUND_03() : '../_levels/0/level_0_16x16._background_03.csv',
    LevelType.BACKGROUND_02() : '../_levels/0/level_0_16x16._background_02.csv',
    LevelType.BACKGROUND_01() : '../_levels/0/level_0_16x16._background_01.csv',
    LevelType.BACK() : '../_levels/0/level_0_16x16._back_tree.csv',
    LevelProperties.NODE_POS() : (500, screen_height / 2),
    LevelProperties.UNLOCK() : 2,
    LevelProperties.NODE_PNG() : '../_assets/overworld/Level02.png',
    LevelProperties.NODE_LOCK() : '../_assets/overworld/LevelLocl.png'
}
level_2 = {
    LevelType.TERRAIN() : '../_levels/0/level_0_16x16._terrain.csv',
    LevelType.PLAYER() : '../_levels/0/level_0_16x16._player_title.csv',
    LevelType.FRONT() : '../_levels/0/level_0_16x16._front_tree.csv',
    LevelType.ENEMY() : '../_levels/0/level_0_16x16._enemy.csv',
    LevelType.CONSTRAINTS() : '../_levels/0/level_0_16x16._constraints.csv',
    LevelType.COLLECTIBLE() : '../_levels/0/level_0_16x16._collectible.csv',
    LevelType.BACKGROUND_06() : '../_levels/0/level_0_16x16._background_06.csv',
    LevelType.BACKGROUND_05() : '../_levels/0/level_0_16x16._background_05.csv',
    LevelType.BACKGROUND_04() : '../_levels/0/level_0_16x16._background_04.csv',
    LevelType.BACKGROUND_03() : '../_levels/0/level_0_16x16._background_03.csv',
    LevelType.BACKGROUND_02() : '../_levels/0/level_0_16x16._background_02.csv',
    LevelType.BACKGROUND_01() : '../_levels/0/level_0_16x16._background_01.csv',
    LevelType.BACK() : '../_levels/0/level_0_16x16._back_tree.csv',
    LevelProperties.NODE_POS() : (800, screen_height / 2),
    LevelProperties.UNLOCK() : 3,
    LevelProperties.NODE_PNG() : '../_assets/overworld/Level03.png',
    LevelProperties.NODE_LOCK() : '../_assets/overworld/LevelLocl.png'
}
level_3 = {
    LevelType.TERRAIN() : '../_levels/0/level_0_16x16._terrain.csv',
    LevelType.PLAYER() : '../_levels/0/level_0_16x16._player_title.csv',
    LevelType.FRONT() : '../_levels/0/level_0_16x16._front_tree.csv',
    LevelType.ENEMY() : '../_levels/0/level_0_16x16._enemy.csv',
    LevelType.CONSTRAINTS() : '../_levels/0/level_0_16x16._constraints.csv',
    LevelType.COLLECTIBLE() : '../_levels/0/level_0_16x16._collectible.csv',
    LevelType.BACKGROUND_06() : '../_levels/0/level_0_16x16._background_06.csv',
    LevelType.BACKGROUND_05() : '../_levels/0/level_0_16x16._background_05.csv',
    LevelType.BACKGROUND_04() : '../_levels/0/level_0_16x16._background_04.csv',
    LevelType.BACKGROUND_03() : '../_levels/0/level_0_16x16._background_03.csv',
    LevelType.BACKGROUND_02() : '../_levels/0/level_0_16x16._background_02.csv',
    LevelType.BACKGROUND_01() : '../_levels/0/level_0_16x16._background_01.csv',
    LevelType.BACK() : '../_levels/0/level_0_16x16._back_tree.csv',
    LevelProperties.NODE_POS() : (1100, screen_height / 2),
    LevelProperties.UNLOCK() : 4,
    LevelProperties.NODE_PNG() : '../_assets/overworld/Level04.png',
    LevelProperties.NODE_LOCK() : '../_assets/overworld/LevelLocl.png'
}

levels = {
    0 : level_0,
    1 : level_1,
    2 : level_2,
    3 : level_3
}