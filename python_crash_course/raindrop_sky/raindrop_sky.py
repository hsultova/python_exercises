import random
import sys

import pygame

from raindrop import Raindrop
from settings import Settings

class RaindropSky:
    """Overall class that manages the raindrop sky."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Raindrop sky')

        self.raindrops = pygame.sprite.Group()
        self._create_raindrops()

        self.pause_raindrops = False
        self.frame_counter = 0

    def _chek_events(self):
        """Handling keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.pause_raindrops = not self.pause_raindrops

    def _create_raindrops(self):
        """Fill the sky with the raindrops."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        random_number = random.uniform(1.0, 5.0)
        current_x, current_y = raindrop_width * random_number, raindrop_height
        while current_y < (self.settings.screen_height - 6 * raindrop_height):
            while current_x < (self.settings.screen_width - 2 * raindrop_width):
                self._create_raindrop(current_x, current_y)
                current_x += 2 * raindrop_width * random_number
            current_x = raindrop_width * random_number
            current_y += raindrop_height * random_number

    def _create_raindrop(self, x_position, y_position):
        """Create a raindrop and place it in the row."""
        new_raindrop = Raindrop(self)
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.raindrops.add(new_raindrop)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.background_color) 
        self.raindrops.draw(self.screen)

        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._chek_events()

            self.frame_counter +=1

            if not self.pause_raindrops and self.frame_counter % 5 == 0:
                self._create_raindrops()

            self.raindrops.update()
            self._update_screen()
            self.clock.tick(self.settings.framerate)


if __name__ == '__main__':
    raindrop_sky = RaindropSky()
    raindrop_sky.run_game()    