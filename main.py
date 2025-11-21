import sys
import os

# Ensure we can import from src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.game_engine import GameEngine

if __name__ == "__main__":
    game = GameEngine()
    game.run()
