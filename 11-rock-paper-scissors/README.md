# ✊✋✌ Python Rock Paper Scissors Game

A command-line Rock Paper Scissors game built using Python where the user plays against the computer.

---

## 📌 Description

This program allows the player to choose:

- rock
- paper
- scissor

The computer randomly selects one option from the same list.

The program then determines:
- Win
- Lose
- Tie

The player can continue playing until they choose to exit.

---

## 🛠 Concepts Used

- `import random`
- `random.choice()`
- Tuples
- While loops
- Nested loops
- Conditional statements (`if-elif-else`)
- Input validation
- Boolean flag control
- String methods (`.lower()`)

---

## 🧠 Program Logic

1. A tuple named `options` stores valid choices.
2. The computer randomly selects an option using `random.choice()`.
3. A nested loop ensures the player enters a valid option.
4. The program compares player and computer choices.
5. The winner is determined based on game rules.
6. The player is asked whether they want to play again.
7. The game continues until the player chooses to quit.

---

## 🎮 Game Rules

- Rock beats Scissor
- Scissor beats Paper
- Paper beats Rock
- Same choices result in a tie

---

## ▶ How to Run

1. Open terminal inside the project folder.
2. Run:

```
python main.py
```

3. Enter your choice when prompted.
4. Choose `y` to play again or `n` to exit.

---

## 💡 Example Output

```
enter your choice (rock, paper , scissors) : rock
player : rock
computer : scissor
You Win

play again (y/n) ? : y
```

---

## 🚀 Project Level

Intermediate Beginner – Demonstrates randomness, input validation, conditional logic, and interactive game design using Python.