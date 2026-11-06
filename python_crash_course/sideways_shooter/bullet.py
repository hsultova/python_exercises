import pygame

from pygame.sprite import Sprite

from ship import Ship
from shooter_settings import Settings

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, screen: pygame.Surface, settings: Settings, ship: Ship) -> None:
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.color = settings.bullet_color

        self.rect: pygame.Rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)