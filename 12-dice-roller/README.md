# 🎲 Python Dice Roller (ASCII Version)

A command-line dice rolling simulator built using Python that visually displays dice faces using ASCII art.

---

## 📌 Description

This program allows the user to:

- Choose how many dice to roll
- Generate random dice values
- Display dice visually using ASCII art
- Calculate and display the total value

Unlike a simple dice roller, this version prints dice side-by-side using structured ASCII graphics.

---

## 🛠 Concepts Used

- `import random`
- `random.randint()`
- Dictionaries
- Tuples
- Lists
- Nested loops
- Dictionary `.get()` method
- Accumulator pattern
- Formatted printing

---

## 🧠 Program Logic

1. A dictionary (`dice_art`) stores ASCII representations of dice faces.
2. The user inputs how many dice they want to roll.
3. Random numbers between 1 and 6 are generated.
4. The dice faces are printed side-by-side using nested loops.
5. The total of all dice values is calculated and displayed.

---

## ▶ How to Run

1. Open terminal inside the project folder.
2. Run:

```
python main.py
```

3. Enter the number of dice when prompted.

---

## 💡 Example Output

```
How many dice?: 2

┌─────────┐┌─────────┐
│  ●   ●  ││    ●    │
│         ││         │
│  ●   ●  ││    ●    │
└─────────┘└─────────┘

Total: 6
```

---

## 🚀 Project Level

Intermediate Beginner – Demonstrates structured data storage, nested loops, visual formatting, and multi-dice simulation using Python.