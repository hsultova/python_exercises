class Settings:
    """"A class to store all settings for Sideways Shooter."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (60, 60, 70)
        
        self.framerate = 60

        # Ship settings
        self.ship_speed = 7.0