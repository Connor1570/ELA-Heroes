from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_BG_MAIN, FONT_SIZE_HEADER, FONT_SIZE_TEXT, STATE_MENU
from src.ui_components import Button, TextLabel, CharacterSprite
from src.word_data import WORD_DATA
import random

class SightWordsGame:
    def __init__(self, engine):
        self.engine = engine
        
        # Get words for current grade, fallback to K if not found
        grade_data = WORD_DATA.get(self.engine.current_grade, WORD_DATA["K"])
        self.words = grade_data.get("sight_words", WORD_DATA["K"]["sight_words"])
        
        self.current_word = ""
        self.options = []
        self.score = 0
        self.message = f"Find the word! (Grade {self.engine.current_grade})"
        self.option_buttons = []
        
        # Character
        self.character = CharacterSprite("assets/images/owlbert.png", 100, SCREEN_HEIGHT - 150)
        
        # Back button
        self.back_button = Button(20, 20, 100, 50, "Back", action=lambda: self.engine.set_state(STATE_MENU))
        
        self.next_round()

    def next_round(self):
        self.current_word = random.choice(self.words)
        # Generate options (correct + 2 random)
        distractors = [w for w in self.words if w != self.current_word]
        self.options = random.sample(distractors, 2) + [self.current_word]
        random.shuffle(self.options)
        self.update_buttons()
        self.message = f"Find: {self.current_word}"

    def update_buttons(self):
        self.option_buttons = []
        start_x = (SCREEN_WIDTH - (3 * 200 + 2 * 50)) // 2
        
        for i, word in enumerate(self.options):
            x = start_x + i * (200 + 50)
            btn = Button(x, 400, 200, 100, word, action=lambda w=word: self.check_answer(w))
            self.option_buttons.append(btn)

    def check_answer(self, selected_word):
        if selected_word == self.current_word:
            self.score += 1
            self.message = "Hoot Hoot! You are wise!"
            self.character.jump() # Animate character
            self.next_round()
        else:
            # Keep showing the target word for autism-friendly support
            self.message = f"Try again! Look for: {self.current_word}"

    def update(self):
        self.character.update()

    def draw(self, surface):
        surface.fill(COLOR_BG_MAIN)
        
        # Draw Character
        self.character.draw(surface)
        
        # Header
        title = TextLabel(SCREEN_WIDTH // 2, 50, "Sight Words with Owlbert", FONT_SIZE_HEADER, center=True)
        title.draw(surface)
        
        # Score (moved to bottom left to avoid overlap)
        score_label = TextLabel(20, SCREEN_HEIGHT - 30, f"Score: {self.score}", FONT_SIZE_TEXT)
        score_label.draw(surface)
        
        # Message
        msg_label = TextLabel(SCREEN_WIDTH // 2, 200, self.message, FONT_SIZE_TEXT, center=True)
        msg_label.draw(surface)
        
        # Options
        for btn in self.option_buttons:
            btn.draw(surface)
            
        # Back Button
        self.back_button.draw(surface)
        
    def handle_event(self, event):
        # Handle back button first
        if self.back_button.handle_event(event):
            return
        
        # Handle option buttons
        for btn in self.option_buttons:
            if btn.handle_event(event):
                return

