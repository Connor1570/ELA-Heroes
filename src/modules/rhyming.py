from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_BG_MAIN, FONT_SIZE_HEADER, FONT_SIZE_TEXT, STATE_MENU
from src.ui_components import Button, TextLabel, CharacterSprite
from src.word_data import WORD_DATA
import random

class RhymingGame:
    def __init__(self, engine):
        self.engine = engine
        
        # Get rhyming pairs for current grade
        grade_data = WORD_DATA.get(self.engine.current_grade, WORD_DATA["K"])
        self.pairs = grade_data.get("rhyming", WORD_DATA["K"]["rhyming"])
        
        self.current_pair = None
        self.options = []
        self.score = 0
        self.message = f"Find the rhyme! (Grade {self.engine.current_grade})"
        self.option_buttons = []
        
        # Character
        self.character = CharacterSprite("assets/images/rhythm_rabbit.png", 100, SCREEN_HEIGHT - 150)
        
        # Back button
        self.back_button = Button(20, 20, 100, 50, "Back", action=lambda: self.engine.set_state(STATE_MENU))
        
        self.next_round()

    def next_round(self):
        self.current_pair = random.choice(self.pairs)
        target_word = self.current_pair[0]
        correct_answer = self.current_pair[1]
        
        # Generate options
        all_rhymes = [p[1] for p in self.pairs]
        distractors = [w for w in all_rhymes if w != correct_answer]
        self.options = random.sample(distractors, 2) + [correct_answer]
        random.shuffle(self.options)
        
        self.update_buttons(correct_answer)
        self.message = f"What rhymes with: {target_word}?"

    def update_buttons(self, correct_answer):
        self.option_buttons = []
        start_x = (SCREEN_WIDTH - (3 * 200 + 2 * 50)) // 2
        
        for i, word in enumerate(self.options):
            x = start_x + i * (200 + 50)
            btn = Button(x, 400, 200, 100, word, action=lambda w=word, c=correct_answer: self.check_answer(w, c))
            self.option_buttons.append(btn)

    def check_answer(self, selected_word, correct_word):
        if selected_word == correct_word:
            self.score += 1
            self.message = "Hippity Hop! That matches!"
            self.character.jump()
            self.next_round()
        else:
            # Keep showing the target word for autism-friendly support
            target_word = self.current_pair[0]
            self.message = f"Try again! What rhymes with: {target_word}?"

    def update(self):
        self.character.update()

    def draw(self, surface):
        surface.fill(COLOR_BG_MAIN)
        
        # Draw Character
        self.character.draw(surface)
        
        # Header
        title = TextLabel(SCREEN_WIDTH // 2, 50, "Rhyming with Rhythm", FONT_SIZE_HEADER, center=True)
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

