from shooter_settings import Settings


class GameStats:
    """Track statistics for the Sideways Shooter game."""
    
    def __init__(self, settings: Settings) -> None:
        """Initialize statistics."""
        self.settings = settings
        self.reset_stats()

        # Start Sideways Shooter in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit