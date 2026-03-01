# 🎯 Python Hangman Game

A command-line Hangman game built using Python with dynamic word selection and ASCII art visualization.

---

## 📌 Description

This program implements the classic Hangman word guessing game.

Features include:

- Random word selection from an external word list
- ASCII art display of hangman stages
- Letter-by-letter guessing
- Input validation
- Win/Loss detection
- Tracking of previously guessed letters

The player must guess the hidden word before running out of attempts.

---

## 🎮 How the Game Works

1. A random word is selected from `words16`.
2. The word is hidden using underscores (`_`).
3. The player guesses one letter at a time.
4. If the guess is correct:
   - All matching letters are revealed.
5. If incorrect:
   - The hangman drawing progresses.
6. The game ends when:
   - The word is fully guessed → **YOU WIN**
   - Maximum wrong guesses reached → **YOU LOSE**

---

## 🛠 Concepts Used

- `import random`
- External module import (`from words16 import words`)
- Dictionaries (for ASCII art stages)
- Lists
- Sets (to track guessed letters)
- While loops
- Conditional statements
- Input validation using `.isalpha()`
- Game state management
- String joining (`" ".join()`)

---

## 🧠 Program Structure

### Functions Included:

- `display_man(wrong_guesses)`  
  Displays hangman ASCII art based on incorrect guesses.

- `display_hint(hint)`  
  Displays current guessed word state.

- `display_answer(answer)`  
  Reveals the correct word at the end.

- `main()`  
  Controls game flow and logic.

---

## ▶ How to Run

1. Make sure `words16.py` exists and contains a list named `words`.
2. Open terminal inside the project folder.
3. Run:

```
python main.py
```

4. Enter one letter at a time to guess the word.

---

## 💡 Example Output

```
*************
 o
 /|\
 / \
*************
_ a _ _ m a _
enter your guessed letter : n
```

Final result:

```
YOU WIN!
```

or

```
YOU LOSE!
```

---

## 🚀 Project Level

Intermediate – Demonstrates structured programming, state management, external file integration, and interactive game development using Python.