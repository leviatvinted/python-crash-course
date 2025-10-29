import pygame

class Character():

    def __init__(self, default_settings, screen):
        """Initialize the character and set its starting position."""
        self.screen = screen
        self.default_settings = default_settings

        # Load the character image and get its rect.
        self.image = pygame.image.load('images/alien_2.bmp')
        self.image = pygame.transform.scale(self.image, (69, 69))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new character at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the character's center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the character's position based on the movement flag"""
        speed = self.default_settings.character_speed_factor

        # Update the character's horizontal center (centerx).
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += speed
        
        if self.moving_left and self.rect.left > 0:
            self.centerx -= speed

        # Update the character's vertical center (centery).
        if self.moving_up and self.rect.top > 0:
            self.centery -= speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += speed

        # Update rect object from self.center.
        self.rect.centerx = int(self.centerx)
        self.rect.centery = int(self.centery)
    
    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)
