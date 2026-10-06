# Hangman Game 🎮

A simple command-line **Hangman game developed in Python**.

The program randomly selects a word and asks the player to guess it letter by letter. Each incorrect answer progressively draws the hangman until the player reaches the maximum number of attempts.

---

## About the Project

This project was developed to practice fundamental Python programming concepts through the implementation of the classic **Hangman word guessing game**.

The game runs directly in the terminal and randomly selects a word from a predefined dictionary.

The player must guess the correct letters before reaching the maximum number of incorrect attempts.

---

## Features

- Random word selection
- Letter-by-letter guessing
- Tracking of previously guessed letters
- Progressive ASCII Hangman drawing
- Limited number of incorrect attempts
- Terminal-based interaction
- Simple word dictionary

---

## Technologies

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)

The project uses only the Python standard library.

Main module used:

```python
import random
```

No external dependencies are required.

---

## How the Game Works

1. The program randomly selects a word from a predefined list.
2. The hidden word is displayed using underscores.
3. The player enters one letter at a time.
4. Correct guesses reveal letters from the word.
5. Incorrect guesses progressively build the Hangman figure.
6. The game ends after six incorrect attempts or when the word is completed.

Example:

```text
Welcome to Hangman

_ _ _ _ _

Letters guessed so far:
a e

Guess a letter: l
```

The Hangman evolves after incorrect guesses:

```text
+---+
 o  |
/|\ |
/ \ |
   ===
```

---

## Project Structure

```text
Hangman/
│
└── hangmangame.py
```

`hangmangame.py` contains the complete game logic.

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

---

## Run the Game

Make sure Python is installed on your computer.

Then run:

```bash
python hangmangame.py
```

Depending on your environment, you may need:

```bash
python3 hangmangame.py
```

---

## Concepts Practiced

This project demonstrates basic Python concepts including:

- Variables
- Lists
- Loops
- Conditional statements
- Functions
- User input
- String manipulation
- Random selection
- Basic game logic
- ASCII-based terminal output

---

## Possible Improvements

Future improvements could include:

- Better validation of user input
- Prevention of duplicate guesses
- Difficulty levels
- Larger word dictionaries
- Word categories
- Score system
- Replay option
- Graphical interface
- Improved win and lose messages

---

## Author

**Hanae KHAYYI**

Data & AI Engineering Student

GitHub: [@hanaekhayyi](https://github.com/hanaekhayyi)

---

⭐ If you found this project useful, feel free to star the repository.
