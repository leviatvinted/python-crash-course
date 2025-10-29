class Settings():
    """A class to store all settings for Space Exploration"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 10, 40) # Deep dark blue

        # Character settings
        self.character_speed_factor = 1.5
