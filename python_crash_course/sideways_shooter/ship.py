import pygame

from shooter_settings import Settings

class Ship:
    """A class to represent the player's ship."""

    def __init__(self, screen: pygame.Surface, settings: Settings) -> None:
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.settings = settings

        self.screen_rect: pygame.Rect = screen.get_rect()
        self.image = pygame.image.load('images/player.png')

        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_rect.centery

        self.y = float(self.rect.y)
        
        self.moving_up = False
        self.moving_down = False

    def draw(self):
        """Draw the ship at its curent location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on movement flags."""  
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y
