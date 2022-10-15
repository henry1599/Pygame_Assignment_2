import pygame as pg

class UI:
    def __init__(self, surface):
        self.display_surface = surface
        
        self.health_bar = pg.image.load('../_assets/UI/health_bar01.png').convert_alpha()
        health_bar_scale = 2
        self.health_bar = pg.transform.scale(self.health_bar, (self.health_bar.get_size()[0] * health_bar_scale, self.health_bar.get_size()[1] * health_bar_scale))
        self.health_bar_topleft = (24, 24)
        self.bar_max_width = 248
        self.bar_height = 24

        self.coin = pg.image.load('../_levels/png/coin.png').convert_alpha()
        self.coin = pg.transform.scale(self.coin, (30, 30))
        self.coin_rect = self.coin.get_rect(topleft = (20, 70))

        self.font = pg.font.Font('../_assets/UI/ARCADEPI.ttf', 30)

    def show_health(self, current_health, max_health):
        self.display_surface.blit(self.health_bar, (20, 20))
        current_health_ratio = current_health / max_health
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pg.Rect(self.health_bar_topleft,(current_bar_width, self.bar_height))
        pg.draw.rect(self.display_surface, 'red', health_bar_rect)

    def show_coin(self, amount):
        self.display_surface.blit(self.coin, self.coin_rect)
        coin_amount_surface = self.font.render(str(amount), False, 'white')
        coin_amount_rect = coin_amount_surface.get_rect(midleft = (self.coin_rect.right + 15, self.coin_rect.centery + 2.5))
        self.display_surface.blit(coin_amount_surface, coin_amount_rect)