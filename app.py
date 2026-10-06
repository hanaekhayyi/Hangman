import streamlit as st
import random

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Hangman Game",
    page_icon="🎮",
    layout="centered"
)

# -----------------------------
# Words
# -----------------------------
WORDS = [
    "sunflower",
    "diamond",
    "hello",
    "cute",
    "bureau",
    "python",
    "computer",
    "developer",
    "artificial",
    "intelligence"
]

# -----------------------------
# Hangman drawings
# -----------------------------
HANGMAN = [
"""
+---+
    |
    |
    |
   ===
""",
"""
+---+
o   |
    |
    |
   ===
""",
"""
+---+
o   |
|   |
    |
   ===
""",
"""
+---+
 o  |
/|  |
    |
   ===
""",
"""
+---+
 o  |
/|\\ |
    |
   ===
""",
"""
+---+
 o  |
/|\\ |
/   |
   ===
""",
"""
+---+
 o  |
/|\\ |
/ \\ |
   ===
"""
]

# -----------------------------
# Initialize game
# -----------------------------
def new_game():
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed_letters = []
    st.session_state.wrong_guesses = 0
    st.session_state.game_over = False


if "word" not in st.session_state:
    new_game()

word = st.session_state.word
guessed_letters = st.session_state.guessed_letters

# -----------------------------
# Title
# -----------------------------
st.title("🎮 Hangman Game")

st.write(
    "Guess the hidden word one letter at a time before the Hangman is completed."
)

# -----------------------------
# Hangman
# -----------------------------
st.code(HANGMAN[st.session_state.wrong_guesses])

# -----------------------------
# Hidden word
# -----------------------------
display_word = " ".join(
    letter.upper() if letter in guessed_letters else "_"
    for letter in word
)

st.markdown(
    f"<h2 style='text-align:center'>{display_word}</h2>",
    unsafe_allow_html=True
)

# -----------------------------
# Game information
# -----------------------------
st.write(
    f"**Wrong guesses:** {st.session_state.wrong_guesses}/6"
)

if guessed_letters:
    st.write(
        "**Letters guessed:**",
        " ".join(letter.upper() for letter in guessed_letters)
    )

# -----------------------------
# Check win / lose
# -----------------------------
won = all(letter in guessed_letters for letter in word)

if won:
    st.success(f"🎉 Congratulations! The word was **{word.upper()}**.")
    st.session_state.game_over = True

elif st.session_state.wrong_guesses >= 6:
    st.error(f"💀 Game Over! The word was **{word.upper()}**.")
    st.session_state.game_over = True

# -----------------------------
# Letter input
# -----------------------------
if not st.session_state.game_over:

    letter = st.text_input(
        "Guess a letter",
        max_chars=1
    ).lower()

    if st.button("Submit guess"):

        if not letter.isalpha() or len(letter) != 1:

            st.warning("Please enter one valid letter.")

        elif letter in guessed_letters:

            st.warning("You already guessed this letter.")

        else:

            st.session_state.guessed_letters.append(letter)

            if letter not in word:
                st.session_state.wrong_guesses += 1

            st.rerun()

# -----------------------------
# Restart
# -----------------------------
st.divider()

if st.button("🔄 New Game"):
    new_game()
    st.rerun()
