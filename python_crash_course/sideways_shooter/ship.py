import pygame

from shooter_settings import Settings

class Ship:
    """A class to represent the player's ship."""

    def __init__(self, screen: pygame.Surface, settings: Settings) -> None:
        self.screen = screen
        self.settings = settings

        self.screen_rect: pygame.Rect = screen.get_rect()
        self.image = pygame.image.load('images/player.png')

        self.image_rect = self.image.get_rect()
        self.image_rect.centery = self.screen_rect.centery

        self.y = float(self.image_rect.y)
        
        self.moving_up = False
        self.moving_down = False

    def draw(self):
        """Draw the ship at its curent location"""
        self.screen.blit(self.image, self.image_rect)

    def update(self):
        """Update the ship's position based on movement flags."""  
        if self.moving_up and self.image_rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.image_rect.y = self.y
