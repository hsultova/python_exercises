class Settings:
    """"A class to store all settings for Sideways Shooter."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (120, 145, 180)
        
        self.framerate = 60

        # Ship settings
        self.ship_speed = 7.0

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_speed = 3.5
        self.bullet_color = (220, 175, 155)

        # Enemy settings
        self.enemy_width = 80
        self.enemy_height = 80
        self.enemy_spawn_count = 5
        self.enemy_speed = 2.0