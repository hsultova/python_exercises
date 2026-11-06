import random
import sys

import pygame

from bullet import Bullet
from enemy import Enemy
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
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self._spawn_enemies_at_random()

    def run(self):
        """Run the game."""
        while True:
            self._chek_events()
            self.ship.update()
            self._update_bullets()
            self.enemies.update()

            self._update_screen()

            self.clock.tick(self.settings.framerate)

    def _update_screen(self):
        """Update the screen during each pass through the loop."""
        self.screen.fill(self.settings.background_color)
        self.ship.draw()
        self.enemies.draw(self.screen)
        
        for bullet in self.bullets.sprites():
            bullet.draw()
        
        pygame.display.flip() 

    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets."""
        self.bullets.update()
        self._check_bullet_enemy_collisions()

        # Get rid of bullets that have disappeared off the screen
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)    

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event: pygame.Event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self.screen, self.settings, self.ship)
        self.bullets.add(new_bullet)

    def _create_enemy(self, x_position: float, y_position: float):
        """Create a new enemy and add it to the enemies group."""
        new_enemy = Enemy(self.screen, self.settings)
        new_enemy.x = x_position
        new_enemy.rect.x = x_position
        new_enemy.rect.y = y_position
        self.enemies.add(new_enemy)

    def _spawn_enemies_at_random(self):
        """Spawn enemies at random positions on the right side of the screen."""
        half_width = self.settings.screen_width // 2

        for _ in range(self.settings.enemy_spawn_count):
            random_x = random.randint(half_width, self.settings.screen_width - self.settings.enemy_size)
            random_y = random.randint(0, self.settings.screen_height -  self.settings.enemy_size)
            self._create_enemy(random_x, random_y)

    def _check_bullet_enemy_collisions(self):
        """Check for collisions between bullets and enemies."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        if collisions:
            for enemies in collisions.values():
                for enemy in enemies:
                    self.enemies.remove(enemy)

if __name__ == "__main__":
    game = SidewaysShooter()
    game.run()