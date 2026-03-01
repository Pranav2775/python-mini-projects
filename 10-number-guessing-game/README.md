# 🎯 Python Number Guessing Game

A command-line number guessing game built using Python.

---

## 📌 Description

This program generates a random number between a specified range (1–100).

The user must guess the correct number.

The program provides feedback after each guess:

- "too low"
- "too high"
- "out of range"
- "invalid guess"

The game continues until the correct number is guessed.

---

## 🛠 Concepts Used

- `import random`
- `random.randint()`
- While loops
- Boolean flag control (`is_running`)
- Input validation using `.isdigit()`
- Conditional statements (`if-elif-else`)
- Range checking
- Guess counter

---

## 🧠 Program Logic

1. The program generates a random number between 1 and 100.
2. The user enters a guess.
3. The program:
   - Checks if input is numeric
   - Checks if guess is within range
   - Compares guess with correct answer
4. The number of guesses is counted.
5. When the correct number is guessed:
   - The answer is revealed
   - Total guesses are displayed
   - The game ends

---

## ▶ How to Run

1. Open terminal inside the project folder.
2. Run:

```
python main.py
```

3. Enter your guesses when prompted.

---

## 💡 Example Output

```
Python Number guessing game
select a number between 1 and 100

Enter your guess: 50
too low

Enter your guess: 75
too high

Enter your guess: 63
correct , the answer was 63
the no of guesses are 3
```

---

## 🚀 Project Level

Intermediate Beginner – Demonstrates randomness, input validation, loop control, and game logic in Python.