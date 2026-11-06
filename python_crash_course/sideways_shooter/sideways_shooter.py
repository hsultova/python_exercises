import sys

import pygame

from ship import Ship
from shooter_settings import Settings

class SidewaysShooter:
    """A class to manage the game assets and behavior for the Sideways Shooter game."""

    def __init__(self):
        """Initialize the game assets and settings."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Sideways Shooter')

        self.ship = Ship(self.screen, self.settings)

    def run(self):
        """Run the game."""
        while True:
            self._chek_events()
            self.ship.update()
            self._update_screen()

            self.clock.tick(self.settings.framerate)

    def _update_screen(self):
        """Update the screen during each pass through the loop."""
        self.screen.fill(self.settings.background_color)
        self.ship.draw()
        pygame.display.flip()     

    def _chek_events(self):
        """Handling keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event: pygame.Event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit() 
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def _check_keyup_events(self, event: pygame.Event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

if __name__ == "__main__":
    game = SidewaysShooter()
    game.run()