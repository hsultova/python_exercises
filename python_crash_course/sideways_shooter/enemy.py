import pygame

from pygame.sprite import Sprite
from shooter_settings import Settings

class Enemy(Sprite):
    def __init__(self, screen: pygame.Surface, settings: Settings) -> None:
        """Initialize the enemy and set its starting position."""
        super().__init__()

        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('images/spaceship.png')
        self.image: pygame.Surface = pygame.transform.scale(self.image, (settings.enemy_size, settings.enemy_size))
        self.rect: pygame.Rect = self.image.get_rect()

        self.rect.x = self.settings.screen_width
        self.rect.y = 0

        self.x = float(self.rect.x)

    def update(self) -> None:
        """Move the enemy across the screen."""
        self.x -= self.settings.enemy_speed
        self.rect.x = self.x