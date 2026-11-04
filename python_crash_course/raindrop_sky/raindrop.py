import random

import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """Manage a raindrop falling from the sky."""

    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load('images/flare.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect: pygame.Rect = self.image.get_rect()

        self.drop_speed = random.uniform(2.0, 5.0)

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrop down."""
        self.y += self.drop_speed
        self.rect.y = self.y

