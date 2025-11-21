from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_BG_MAIN, FONT_SIZE_HEADER, FONT_SIZE_TEXT, COLOR_ACCENT, STATE_MENU
from src.ui_components import Button, TextLabel, CharacterSprite
from src.word_data import WORD_DATA
import random

class CVCBlendingGame:
    def __init__(self, engine):
        self.engine = engine
        
        # Get CVC words for current grade
        grade_data = WORD_DATA.get(self.engine.current_grade, WORD_DATA["K"])
        self.words = grade_data.get("cvc", WORD_DATA["K"]["cvc"])
        
        self.current_word = ""
        self.scrambled_letters = []
        self.built_word = ""
        self.score = 0
        self.message = f"Build the word! (Grade {self.engine.current_grade})"
        self.letter_buttons = []
        
        # Character
        self.character = CharacterSprite("assets/images/builder_bear.png", 100, SCREEN_HEIGHT - 150)
        
        # Back button
        self.back_button = Button(20, 20, 100, 50, "Back", action=lambda: self.engine.set_state(STATE_MENU))
        
        self.next_round()

    def next_round(self):
        self.current_word = random.choice(self.words)
        self.built_word = ""
        self.scrambled_letters = list(self.current_word)
        random.shuffle(self.scrambled_letters)
        self.update_buttons()
        self.message = f"Build: {self.current_word.upper()}"

    def update_buttons(self):
        self.letter_buttons = []
        
        # Dynamic sizing for longer words
        num_letters = len(self.scrambled_letters)
        max_width = SCREEN_WIDTH - 100 # Keep some padding
        
        # Default size
        btn_width = 100
        spacing = 20
        
        total_width = num_letters * btn_width + (num_letters - 1) * spacing
        
        # Scale down if too wide
        if total_width > max_width:
            scale_factor = max_width / total_width
            btn_width = int(btn_width * scale_factor)
            spacing = int(spacing * scale_factor)
            total_width = max_width

        start_x = (SCREEN_WIDTH - total_width) // 2
        
        for i, char in enumerate(self.scrambled_letters):
            if char is not None:
                x = start_x + i * (btn_width + spacing)
                btn = Button(x, 400, btn_width, 100, char, action=lambda c=char, idx=i: self.letter_clicked(idx, c))
                self.letter_buttons.append(btn)

    def letter_clicked(self, index, char):
        # Check if this is the correct next letter
        target_char = self.current_word[len(self.built_word)]
        
        if char == target_char:
            self.built_word += char
            self.scrambled_letters[index] = None # Remove from available
            self.message = "Good job! Keep building!"
            
            if self.built_word == self.current_word:
                self.score += 1
                self.message = f"You built '{self.current_word.upper()}'!"
                self.character.jump()
                self.next_round()
            else:
                self.update_buttons()
        else:
            # Keep showing the target word for autism-friendly support
            self.message = f"Try a different block. Building: {self.current_word.upper()}"

    def update(self):
        self.character.update()

    def draw(self, surface):
        surface.fill(COLOR_BG_MAIN)
        
        # Draw Character
        self.character.draw(surface)
        
        # Header
        title = TextLabel(SCREEN_WIDTH // 2, 50, "CVC Blending with Builder Bear", FONT_SIZE_HEADER, center=True)
        title.draw(surface)
        
        # Score (moved to bottom left to avoid overlap)
        score_label = TextLabel(20, SCREEN_HEIGHT - 30, f"Score: {self.score}", FONT_SIZE_TEXT)
        score_label.draw(surface)
        
        # Message
        msg_label = TextLabel(SCREEN_WIDTH // 2, 200, self.message, FONT_SIZE_TEXT, center=True)
        msg_label.draw(surface)
        
        # Built Word Display
        built_label = TextLabel(SCREEN_WIDTH // 2, 300, self.built_word.upper(), 60, color=COLOR_ACCENT, center=True)
        built_label.draw(surface)
        
        # Letter Buttons
        for btn in self.letter_buttons:
            btn.draw(surface)
            
        # Back Button
        self.back_button.draw(surface)

    def handle_event(self, event):
        # Handle back button first
        if self.back_button.handle_event(event):
            return
        
        # Handle letter buttons
        for btn in self.letter_buttons:
            if btn.handle_event(event):
                return

