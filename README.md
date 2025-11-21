# ELA Heroes 🦸‍♂️📚

**ELA Heroes** is an engaging, interactive educational game designed to help children in Grades K-6 master English Language Arts concepts. Built with Python and Pygame, it features a friendly cast of characters and an autism-friendly design to make learning accessible and fun for everyone.

## 🎮 Features

*   **4 Unique Game Modules:**
    *   **Sight Words with Owlbert:** Practice high-frequency words with our wise owl friend.
    *   **Rhyming with Rhythm Rabbit:** Find matching rhymes in a fun, bouncy environment.
    *   **CVC Blending with Builder Bear:** Construct words letter-by-letter (and more complex words in higher grades!).
    *   **Word Families with Family Fox:** Sort words into their correct families.
*   **Grade Level Selector (K-6):**
    *   Instantly switch between 7 different grade levels.
    *   Content adapts dynamically: from simple 3-letter words in Kindergarten to complex vocabulary in Grade 6.
*   **Autism-Friendly Design:**
    *   **Gentle Feedback:** Incorrect answers gently guide the student back to the target word, keeping the focus on learning without frustration.
    *   **Reduced Overstimulation:** Animations are event-triggered (e.g., only jumping on success) rather than constant.
    *   **Clean Visuals:** High-contrast text and white backgrounds for characters help focus attention.
*   **Settings:**
    *   Volume control.
    *   High Contrast mode toggle.

## 🚀 Getting Started

### Prerequisites

*   **Windows OS** (for the pre-built executable)
*   **Python 3.10+** (if running from source)

### Running the Game (Easiest Method)

1.  Navigate to the `dist` folder.
2.  Double-click `ELA Heroes.exe`.
3.  **Or** simply run the `Play ELA Heroes.bat` file in the main directory.

### Running from Source

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ela-heroes.git
    cd ela-heroes
    ```
2.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the game:
    ```bash
    python main.py
    ```

## 🛠️ Building the Executable

If you want to build the standalone `.exe` yourself:

1.  Ensure you have the dependencies installed.
2.  Run the build script:
    ```bash
    .\build_exe.bat
    ```
3.  The new executable will be created in the `dist` folder.

## 📂 Project Structure

*   `src/`: Contains all source code.
    *   `game_engine.py`: The core engine managing states and loops.
    *   `ui_components.py`: Reusable UI elements (Buttons, Labels, Sprites).
    *   `word_data.py`: The massive database of words for Grades K-6.
    *   `modules/`: Individual game logic for each subject.
*   `assets/`: Images and resources.
*   `settings.py`: Global configuration (colors, screen size, etc.).

## 👨‍💻 Credits

*   **Created by:** Natalie and Connor Murphy
*   **Development Assistance:** Antigravity (Google DeepMind)
*   **Tech Stack:** Python, Pygame CE

---
*Happy Learning!* 🌟
