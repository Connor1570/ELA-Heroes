import pygame

# Screen Dimensions
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 850
FPS = 60

# Colors (Autism-friendly palette - muted, calming)
# Soft Blues and Greens
COLOR_BG_MAIN = (230, 240, 255)  # Very light blue
COLOR_BG_MENU = (220, 235, 220)  # Light sage green
COLOR_TEXT = (40, 40, 60)        # Dark slate (not pure black)
COLOR_ACCENT = (100, 149, 237)   # Cornflower blue
COLOR_HIGHLIGHT = (255, 215, 0)  # Gold (for success)
COLOR_ERROR = (205, 92, 92)      # Indian Red (soft red)

# Fonts
FONT_MAIN = "Verdana" # Fallback, will load custom later
FONT_SIZE_TITLE = 64
FONT_SIZE_HEADER = 48
FONT_SIZE_TEXT = 32

# Audio
DEFAULT_VOLUME = 0.5

# Game States
STATE_MENU = "menu"
STATE_GAME = "game"
STATE_CREDITS = "credits"
STATE_SETTINGS = "settings"
