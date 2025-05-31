import pygame

class Level:
    def __init__(self):
        # dispaly surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        pass