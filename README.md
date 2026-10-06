# Hangman Game 🎮

A simple **Hangman game developed in Python**, available both as a command-line application and as an interactive web application built with **Streamlit**.

The program randomly selects a word and asks the player to guess it letter by letter. Each incorrect answer progressively draws the Hangman until the player reaches the maximum number of attempts.

---

## About the Project

This project was developed to practice fundamental Python programming concepts through the implementation of the classic **Hangman word guessing game**.

The project includes two versions:

- A **command-line version** running directly in the terminal.
- A **Streamlit web version** providing a more interactive and user-friendly interface.

The game randomly selects a word from a predefined dictionary, and the player must guess the correct letters before reaching the maximum number of incorrect attempts.

---

## Features

- Random word selection
- Letter-by-letter guessing
- Tracking of previously guessed letters
- Progressive ASCII Hangman drawing
- Maximum of six incorrect attempts
- Input validation
- Prevention of duplicate guesses
- Automatic win and loss detection
- Restart / new game option
- Command-line interface
- Interactive Streamlit web interface

---

## Technologies

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?logo=streamlit&logoColor=white)

Main technologies used:

- **Python**
- **Streamlit**
- Python `random` module
- Streamlit `session_state`

The command-line version uses only the Python standard library.

The web version requires Streamlit.

---

## How the Game Works

1. The program randomly selects a word from a predefined list.
2. The hidden word is displayed using underscores.
3. The player enters one letter at a time.
4. Correct guesses reveal the corresponding letters in the word.
5. Incorrect guesses progressively build the Hangman figure.
6. Previously entered letters are tracked.
7. Duplicate guesses are detected.
8. The game ends after six incorrect attempts or when the complete word is guessed.
9. The player can start a new game at any time.

Example:

```text
Welcome to Hangman

_ _ _ _ _

Letters guessed so far:
A E

Guess a letter: L
```

The Hangman progressively evolves after incorrect guesses:

```text
+---+
 o  |
/|\ |
/ \ |
   ===
```

---

## Web Version with Streamlit

The Streamlit version provides an interactive browser-based interface.

It includes:

- Visual representation of the hidden word
- Interactive letter input
- Display of previously guessed letters
- Wrong guess counter
- Dynamic Hangman drawing
- Success message when the word is found
- Game-over message when the maximum number of attempts is reached
- New Game button

Streamlit's `session_state` is used to preserve the game state between user interactions.

---

## Project Structure

```text
Hangman/
│
├── app.py
├── hangmangame.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Files

`hangmangame.py`

Contains the original command-line version of the Hangman game.

`app.py`

Contains the Streamlit web application.

`requirements.txt`

Contains the Python dependencies required to run the Streamlit application.

`README.md`

Contains the project documentation.

`.gitignore`

Prevents unnecessary local and environment files from being pushed to GitHub.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/hanaekhayyi/Hangman.git
```

Navigate to the project directory:

```bash
cd Hangman
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Command-Line Version

Make sure Python is installed on your computer.

Run:

```bash
python hangmangame.py
```

Depending on your environment, you may need:

```bash
python3 hangmangame.py
```

---

## Run the Streamlit Version

To launch the web application:

```bash
streamlit run app.py
```

Streamlit will start a local server and open the application in your browser.

The application is usually available at:

```text
http://localhost:8501
```

---

## Requirements

The `requirements.txt` file contains:

```text
streamlit
```

Install the dependencies with:

```bash
pip install -r requirements.txt
```

---

## Concepts Practiced

This project demonstrates several Python and application development concepts, including:

- Variables
- Lists
- Loops
- Conditional statements
- Functions
- User input
- String manipulation
- Random selection
- Game logic
- ASCII-based terminal output
- Input validation
- State management
- Streamlit components
- Web application development with Python
- Session management using `st.session_state`

---

## Project Evolution

The project was initially developed as a simple terminal-based Python game.

It was then extended into an interactive web application using **Streamlit**.

This evolution demonstrates how a basic Python project can be transformed into a user-friendly web application while keeping the original game logic.

```text
Python CLI
    │
    ▼
Game Logic
    │
    ▼
Streamlit Interface
    │
    ▼
Interactive Web Application
```

---

## Possible Improvements

Future improvements could include:

- Difficulty levels
- Larger word dictionaries
- Word categories
- Score system
- Player statistics
- Hint system
- Timer
- Multiplayer mode
- Leaderboard
- Improved graphical Hangman representation
- Sound effects
- Deployment on Streamlit Community Cloud

---

## Deployment

The Streamlit application can be deployed using **Streamlit Community Cloud**.

Once deployed, the application can be played directly from a browser without installing Python locally.

A live demo link can then be added here:

```text
Live Demo: Coming soon
```

---

## Author

**Hanae KHAYYI**

Data & AI Engineering Student

GitHub: [@hanaekhayyi](https://github.com/hanaekhayyi)

---

⭐ If you found this project useful, feel free to star the repository.
