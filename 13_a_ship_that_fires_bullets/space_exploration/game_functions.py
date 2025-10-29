import sys

import pygame

def check_keydown_events(event, character):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        character.moving_right = True
    elif event.key == pygame.K_LEFT:
        character.moving_left = True
    elif event.key == pygame.K_UP:
        character.moving_up = True
    elif event.key == pygame.K_DOWN:
        character.moving_down = True

def check_keyup_events(event, character):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        character.moving_right = False
    elif event.key == pygame.K_LEFT:
        character.moving_left = False
    elif event.key == pygame.K_UP:
        character.moving_up = False
    elif event.key == pygame.K_DOWN:
        character.moving_down = False       

def check_events(character):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, character)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, character)


def update_screen(default_settings, screen, character):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(default_settings.bg_color)
    character.blitme()
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()
