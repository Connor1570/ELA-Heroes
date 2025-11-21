from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_BG_MAIN, FONT_SIZE_HEADER, FONT_SIZE_TEXT, STATE_MENU
from src.ui_components import Button, TextLabel, CharacterSprite
from src.word_data import WORD_DATA
import random

class WordFamiliesGame:
    def __init__(self, engine):
        self.engine = engine
        
        # Get word families for current grade
        grade_data = WORD_DATA.get(self.engine.current_grade, WORD_DATA["K"])
        self.families = grade_data.get("families", WORD_DATA["K"]["families"])
        
        self.current_family = ""
        self.options = []
        self.score = 0
        self.message = f"Sort the words! (Grade {self.engine.current_grade})"
        self.option_buttons = []
        
        # Character
        self.character = CharacterSprite("assets/images/family_fox.png", 100, SCREEN_HEIGHT - 150)
        
        # Back button
        self.back_button = Button(20, 20, 100, 50, "Back", action=lambda: self.engine.set_state(STATE_MENU))
        
        self.next_round()

    def next_round(self):
        self.current_family = random.choice(list(self.families.keys()))
        correct_word = random.choice(self.families[self.current_family])
        
        # Distractors from other families
        other_families = [f for f in self.families.keys() if f != self.current_family]
        distractors = []
        for _ in range(2):
            fam = random.choice(other_families)
            distractors.append(random.choice(self.families[fam]))
            
        self.options = [correct_word] + distractors
        random.shuffle(self.options)
        
        self.update_buttons(correct_word)
        self.message = f"Find the word in the '{self.current_family.upper()}' family"

    def update_buttons(self, correct_word):
        self.option_buttons = []
        start_x = (SCREEN_WIDTH - (3 * 200 + 2 * 50)) // 2
        
        for i, word in enumerate(self.options):
            x = start_x + i * (200 + 50)
            btn = Button(x, 400, 200, 100, word, action=lambda w=word, c=correct_word: self.check_answer(w, c))
            self.option_buttons.append(btn)

    def check_answer(self, selected_word, correct_word):
        if selected_word == correct_word:
            self.score += 1
            self.message = "Welcome to the family!"
            self.character.jump()
            self.next_round()
        else:
            # Keep showing the target family for autism-friendly support
            self.message = f"Try again! Find a word in the '{self.current_family.upper()}' family"

    def update(self):
        self.character.update()

    def draw(self, surface):
        surface.fill(COLOR_BG_MAIN)
        
        # Draw Character
        self.character.draw(surface)
        
        # Header
        title = TextLabel(SCREEN_WIDTH // 2, 50, "Word Families with Family Fox", FONT_SIZE_HEADER, center=True)
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

