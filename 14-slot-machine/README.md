# 🎰 Python Slot Machine Game

A command-line slot machine game built using Python with emoji-based symbols and dynamic payout logic.

---

## 📌 Description

This program simulates a real slot machine where:

- The player starts with an initial balance of $100
- The player places a bet
- Three random symbols are generated
- The program checks for winning combinations
- The balance is updated based on payout rules
- The game continues until the player exits or runs out of balance

---

## 🎮 Symbols

The slot machine uses the following symbols:

🍒  🍋  🍉  🔔  ⭐

Each symbol has a different payout multiplier.

---

## 💰 Payout Rules

If all three symbols match:

- 🍒 → 3x bet
- 🍋 → 5x bet
- 🍉 → 10x bet
- 🔔 → 20x bet
- ⭐ → 100x bet

If symbols do not match → No payout.

---

## 🛠 Concepts Used

- `import random`
- `random.choice()`
- Lists
- List comprehension
- Functions
- Return values
- While loops
- Conditional statements
- Input validation using `.isdigit()`
- Balance management
- String formatting
- `if __name__ == "__main__"` execution guard

---

## 🧠 Program Structure

### Functions Included:

- `spin_row()`  
  Generates three random symbols.

- `print_row(row)`  
  Displays slot symbols in formatted style.

- `get_payout(row, bet)`  
  Calculates winnings based on symbol match.

- `main()`  
  Controls game flow and balance management.

---

## ▶ How to Run

1. Open terminal inside the project folder.
2. Run:

```
python main.py
```

3. Enter your bet amount.
4. Choose whether to play again.

---

## 💡 Example Output

```
current balance : $100
place your bet : $10

spinning................
**************
🍒 | 🍒 | 🍒
**************

you won : $30
```

---

## 🚀 Project Level

Intermediate – Demonstrates structured programming, payout algorithms, input validation, and game-based balance management in Python.