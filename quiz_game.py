import time
import random
import json  # Added for high scores
from image_display import display_image  # Import the display_image function
from easy_questions import easy_difficulty_questions as easy_questions
from medium_questions import medium_difficulty_questions as medium_questions
from hard_questions import hard_difficulty_questions as hard_questions

# Function to load questions based on difficulty level
def load_questions(difficulty):
    if difficulty == 'EASY':
        return easy_questions
    elif difficulty == 'MEDIUM':
        return medium_questions
    elif difficulty == 'HARD':
        return hard_questions
    else:
        raise ValueError("Invalid difficulty level")
    
# Load high scores from file or initialize an empty list
def load_high_scores():
    try:
        with open('high_scores.json', 'r') as file:
            content = file.read()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON. File might be corrupted. Initializing with an empty list.")
        return []

# Save high scores to file
def save_high_scores(scores):
    with open('12012024-Assignment_One/high_scores.json', 'w') as file:
        json.dump(scores, file)

# Display high scores
def display_high_scores(scores):
    print("\nHigh Scores:")
    for idx, score in enumerate(scores, start=1):
        print(f"{idx}. {score['name']}: {score['score']}")

# Function for typewriter effect
def typewriter_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# User Input and Difficulty Selection
typewriter_print("""
??? Welcome TO ??? GUESS THIS ??? The Interactive Quiz Game, TWISTING YOUR MELON ???

Choose your difficulty level:
1. EASY
2. MEDIUM
3. HARD
""")

difficulty_input = input("Enter the number corresponding to your difficulty level: ")
difficulty_levels = ['EASY', 'MEDIUM', 'HARD']

try:
    difficulty_choice = difficulty_levels[int(difficulty_input) - 1]
except (ValueError, IndexError):
    typewriter_print("Invalid choice. Please choose a valid difficulty level.")
    exit()

questions = load_questions(difficulty_choice)

# Shuffle the questions to present them in a random order
random.shuffle(questions)

# Displaying Game Instructions with Typewriter Effect
instructions_text =f"""
??? Welcome to the Interactive Quiz Game (Difficulty: {difficulty_choice}) ???
      
??? GUESS THIS ???

??? A Game of Fun, Facts, Education, and Most of All, GUESSES!!! Test Yourself with the Ultimate Quiz Adventure. ???

??? Don't be a DONUT!!! - Be a SQUARE and let me take you there ???

??? You will be presented with a series of 50 QUESTIONS ???

??? Choose the CORRECT OPTION, A, B, C, or D, and PRESS ENTER

??? Your TIME is 30 SECONDS PER QUESTION ???

??? Don't GET UPTIGHT, JUST GET EM' ALL RIGHT ???
"""
typewriter_print(instructions_text)

# Initialize the score and question counter
score = 0
question_counter = 0

# Iterate through each question in the list and present it to the user
for idx, question in enumerate(questions, start=1):
    # Increment the question counter
    question_counter += 1

    # Display the question statement
    print(f"\nQuestion {idx}: {question['question']}")

    # Display the answer choices
    for i, choice in enumerate(question['choices'], start=65):  # ASCII code for 'A' is 65
        print(f"{chr(i)}. {choice}")

    # Add a timer
    countdown = 30  # Set the countdown time to 30 seconds
    start_time = time.time()

    user_answer = input("\nYour answer (A/B/C/D): ").upper()
    end_time = time.time()

    # Check if the user answered before the countdown ends
    elapsed_time = end_time - start_time
    remaining_time = max(countdown - elapsed_time, 0)

    if remaining_time == 0:
        print("Time's up!")
    else:
        print(f"Time left: {remaining_time:.2f} seconds")

    # Check if 50 questions have been asked for each difficulty
    if question_counter == 50:
        print(f"You have completed 50 questions in {difficulty_choice} mode. Game over!")
        break

    # Check the answer
    if user_answer.upper() == question['correct_answer'].upper():
        print("CORRECT!!! WHOOP!!! WHOOP!!! WHOOP!!!")
        score += 1
    else:
        print(f"Your answer is WRONG: {user_answer.upper()}, Correct answer: {question['correct_answer'].upper()}")

# Display the result
print("\nQuiz completed!")
print(f"Your final score is: {score} out of {len(questions)}.")

# Display and Update High Scores
high_scores = load_high_scores()
display_high_scores(high_scores)

# Ask for the player's name for the high scores
player_name = input("Enter your name for the high scores: ")

# Add the current score to the high scores
high_scores.append({"name": player_name, "score": score})

# Sort the high scores in descending order
high_scores.sort(key=lambda x: x['score'], reverse=True)

# Keep only the top 10 high scores
high_scores = high_scores[:10]

# Save the updated high scores
print(high_scores)  # Add this line to see the scores before saving
save_high_scores(high_scores)

# Display an image
image_path = "12012024-Assignment_One/GUESS-THIS LOGO-SOLO -128.png"
display_image(image_path)

