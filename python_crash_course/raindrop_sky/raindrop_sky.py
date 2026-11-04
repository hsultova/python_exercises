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

        self.continuous_spawning = False
        self.frame_counter = 0

    def _check_events(self):
        """Handling keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.continuous_spawning = not self.continuous_spawning

    def _create_raindrops(self):
        """Create a full sky of raindrops."""
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

    def _spawn_raindrops_periodically(self):
        """Spawn raindrops to the sky at regular intervals."""
        self.frame_counter += 1
        if self.frame_counter % self.settings.raindrop_update_interval == 0:
            self._create_raindrops()

    def _remove_offscreen_raindrops(self):
        """Remove raindrops that disappeared from the screen."""
        for raindrop in self.raindrops.sprites():
            if raindrop.check_edges():
                raindrop.kill()

    def _spawn_raindrops_if_empty(self):
        """Spawn raindrops to the sky if there are no raindrops."""
        if not self.raindrops:
            self._create_raindrops()

    def _run_spawn_strategy(self):
        """Run the appropriate raindrop spawn strategy."""
        if self.continuous_spawning:
            self._spawn_raindrops_periodically()
        else:            
            self._spawn_raindrops_if_empty()

    def _update_raindrops(self):
        """Update the position of raindrops."""
        self._remove_offscreen_raindrops()
        self._run_spawn_strategy()
        self.raindrops.update()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.background_color) 
        self.raindrops.draw(self.screen)

        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_raindrops()            
            self._update_screen()
            self.clock.tick(self.settings.framerate)

if __name__ == '__main__':
    raindrop_sky = RaindropSky()
    raindrop_sky.run_game()    