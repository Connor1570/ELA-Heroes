import pygame
import sys
from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS, 
    COLOR_BG_MENU, COLOR_BG_MAIN, 
    STATE_MENU, STATE_GAME, STATE_CREDITS, STATE_SETTINGS,
    FONT_SIZE_TITLE, FONT_SIZE_HEADER, FONT_SIZE_TEXT,
    COLOR_TEXT, COLOR_ACCENT, COLOR_HIGHLIGHT
)
from src.ui_components import Button, TextLabel

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("ELA Heroes")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = STATE_MENU
        self.current_module = None
        
        # Settings
        self.current_grade = "K"
        self.grades = ["K", "1", "2", "3", "4", "5", "6"]
        self.volume = 0.5
        self.high_contrast = False
        
        # Initialize fonts
        pygame.font.init()

        # Menu Components
        self.setup_menu()
        self.setup_credits()
        self.setup_settings()

    def setup_menu(self):
        button_width = 600
        x_pos = SCREEN_WIDTH // 2 - button_width // 2
        
        # Grade Selector Button
        self.grade_btn = Button(SCREEN_WIDTH - 200, 20, 180, 50, f"Grade: {self.current_grade}", action=self.cycle_grade, color=COLOR_HIGHLIGHT)
        
        self.menu_buttons = [
            Button(x_pos, 200, button_width, 60, "Sight Words (Owlbert)", action=lambda: self.start_module("sight_words")),
            Button(x_pos, 280, button_width, 60, "Rhyming (Rhythm)", action=lambda: self.start_module("rhyming")),
            Button(x_pos, 360, button_width, 60, "CVC Blending (Builder Bear)", action=lambda: self.start_module("cvc")),
            Button(x_pos, 440, button_width, 60, "Word Families (Family Fox)", action=lambda: self.start_module("families")),
            Button(x_pos, 520, button_width, 60, "Settings", action=lambda: self.set_state(STATE_SETTINGS)),
            Button(x_pos, 600, button_width, 60, "Credits", action=lambda: self.set_state(STATE_CREDITS)),
            Button(x_pos, 680, button_width, 60, "Exit", action=self.quit_game)
        ]
        self.title_label = TextLabel(SCREEN_WIDTH//2, 100, "ELA Heroes", font_size=FONT_SIZE_TITLE, center=True)

    def setup_credits(self):
        self.credits_back_btn = Button(50, 50, 150, 50, "Back", action=lambda: self.set_state(STATE_MENU))
        self.credits_text = [
            TextLabel(SCREEN_WIDTH//2, 200, "Created by:", font_size=FONT_SIZE_HEADER, center=True),
            TextLabel(SCREEN_WIDTH//2, 300, "Natalie and Connor Murphy", font_size=FONT_SIZE_TEXT, center=True),
            TextLabel(SCREEN_WIDTH//2, 350, "with help from Antigravity", font_size=FONT_SIZE_TEXT, center=True),
        ]

    def setup_settings(self):
        self.settings_back_btn = Button(50, 50, 150, 50, "Back", action=lambda: self.set_state(STATE_MENU))
        
        # Volume Controls
        self.volume_label = TextLabel(SCREEN_WIDTH//2, 200, f"Volume: {int(self.volume * 100)}%", font_size=FONT_SIZE_HEADER, center=True)
        self.vol_up_btn = Button(SCREEN_WIDTH//2 + 100, 250, 50, 50, "+", action=lambda: self.change_volume(0.1))
        self.vol_down_btn = Button(SCREEN_WIDTH//2 - 150, 250, 50, 50, "-", action=lambda: self.change_volume(-0.1))
        
        # Contrast Control
        self.contrast_btn = Button(SCREEN_WIDTH//2 - 150, 350, 300, 80, "Toggle High Contrast", action=self.toggle_contrast)
        self.contrast_status = TextLabel(SCREEN_WIDTH//2, 450, f"High Contrast: {'ON' if self.high_contrast else 'OFF'}", font_size=FONT_SIZE_TEXT, center=True)

    def cycle_grade(self):
        current_idx = self.grades.index(self.current_grade)
        next_idx = (current_idx + 1) % len(self.grades)
        self.current_grade = self.grades[next_idx]
        self.grade_btn.text = f"Grade: {self.current_grade}"

    def change_volume(self, change):
        self.volume = max(0.0, min(1.0, self.volume + change))
        self.volume_label.text = f"Volume: {int(self.volume * 100)}%"
        # Here you would set the actual mixer volume if music was implemented
        # pygame.mixer.music.set_volume(self.volume)

    def toggle_contrast(self):
        self.high_contrast = not self.high_contrast
        self.contrast_status.text = f"High Contrast: {'ON' if self.high_contrast else 'OFF'}"
        # In a real implementation, this would trigger a global color update
        # For now, we'll just store the state which modules can check

    def set_state(self, new_state):
        self.state = new_state
        if new_state == STATE_MENU:
            self.current_module = None
            # Update grade button text in case it reset (though it shouldn't)
            self.grade_btn.text = f"Grade: {self.current_grade}"

    def start_module(self, module_name):
        if module_name == "sight_words":
            from src.modules.sight_words import SightWordsGame
            self.current_module = SightWordsGame(self)
        elif module_name == "rhyming":
            from src.modules.rhyming import RhymingGame
            self.current_module = RhymingGame(self)
        elif module_name == "cvc":
            from src.modules.cvc_blending import CVCBlendingGame
            self.current_module = CVCBlendingGame(self)
        elif module_name == "families":
            from src.modules.word_families import WordFamiliesGame
            self.current_module = WordFamiliesGame(self)
        
        self.state = STATE_GAME

    def update(self):
        if self.state == STATE_GAME and self.current_module:
            self.current_module.update()

    def draw(self):
        if self.state == STATE_MENU:
            self.screen.fill(COLOR_BG_MENU)
            self.title_label.draw(self.screen)
            self.grade_btn.draw(self.screen)
            for btn in self.menu_buttons:
                btn.draw(self.screen)
        
        elif self.state == STATE_CREDITS:
            self.screen.fill(COLOR_BG_MAIN)
            self.credits_back_btn.draw(self.screen)
            for label in self.credits_text:
                label.draw(self.screen)

        elif self.state == STATE_SETTINGS:
            self.screen.fill(COLOR_BG_MAIN)
            self.settings_back_btn.draw(self.screen)
            self.volume_label.draw(self.screen)
            self.vol_up_btn.draw(self.screen)
            self.vol_down_btn.draw(self.screen)
            self.contrast_btn.draw(self.screen)
            self.contrast_status.draw(self.screen)
        
        elif self.state == STATE_GAME and self.current_module:
            self.current_module.draw(self.screen)

        pygame.display.flip()

    def quit_game(self):
        self.running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            
            if self.state == STATE_MENU:
                self.grade_btn.handle_event(event)
                for btn in self.menu_buttons:
                    btn.handle_event(event)
            elif self.state == STATE_CREDITS:
                self.credits_back_btn.handle_event(event)
            elif self.state == STATE_SETTINGS:
                self.settings_back_btn.handle_event(event)
                self.vol_up_btn.handle_event(event)
                self.vol_down_btn.handle_event(event)
                self.contrast_btn.handle_event(event)
            elif self.state == STATE_GAME and self.current_module:
                self.current_module.handle_event(event)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
