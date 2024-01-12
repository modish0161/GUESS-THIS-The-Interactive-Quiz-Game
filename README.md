# GUESS THIS: The Interactive Quiz Game

## Overview
GUESS THIS is an interactive quiz game where users answer questions of varying difficulty levels. The game provides feedback on correct or incorrect answers and calculates the final score. High scores are displayed and updated based on user performance.

## Dependencies
- `time`, `random`, `json`: Standard Python libraries for handling time, generating random numbers, and working with JSON data.
- `image_display`: A custom module containing the `display_image` function.
- `easy_questions`, `medium_questions`, `hard_questions`: Modules with questions for different difficulty levels.

## Functionality

### Imported Modules
- `import time, random, json, image_display`: Importing necessary modules for time, randomness, JSON handling, and image display.

### Question Loading
- `load_questions(difficulty)`: Function to load questions based on the specified difficulty level.

### High Scores
- `load_high_scores()`: Load high scores from the `high_scores.json` file or initialize an empty list if the file is not found or corrupted.
- `save_high_scores(scores)`: Save high scores to the `high_scores.json` file.
- `display_high_scores(scores)`: Display high scores to the user.

### Typewriter Effect
- `typewriter_print(text, delay=0.03)`: Function for creating a typewriter effect when printing text.

### User Input and Difficulty Selection
- Prompt the user to choose a difficulty level (Easy, Medium, or Hard) and handle invalid inputs.

### Game Instructions
- Display game instructions with a typewriter effect.

### Quiz Gameplay
- Iterate through each question, present it to the user, and collect their answers within a time limit.
- Provide feedback on correct or incorrect answers.

### Result and High Scores Display
- Display the quiz completion message and the final score.
- Display and update high scores based on user performance.
- Ask for the player's name for high scores and save the updated scores.

### Image Display
- Display the GUESS THIS logo image at the end of the game.

## Usage
1. Ensure that the required modules and dependencies are installed.
2. Run the `quiz_game.py` script to start the game.
3. Follow on-screen instructions to choose a difficulty level and answer questions.

Enjoy playing GUESS THIS!
