import sys
import pygame

from settings import Settings
from character import Character
import game_functions as gf

def run_game():
    # Initialize game and create screen objects
    pygame.init()
    default_settings = Settings()    
    screen = pygame.display.set_mode((
        default_settings.screen_width,
        default_settings.screen_height
    ))
    pygame.display.set_caption("Space Exploration")

    # Make a character.
    character = Character(default_settings, screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(character)
        character.update()
        gf.update_screen(default_settings, screen, character)

run_game()
