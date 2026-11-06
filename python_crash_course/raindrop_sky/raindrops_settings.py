class Settings:
    """A class to store all settings for Raindrop sky."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (69, 74, 125)
        
        self.framerate = 60

        # Raindrops settings
        self.raindrop_spawn_ms = 200