# ⏳ Python Countdown Timer

A simple command-line countdown timer built using Python.

---

## 📌 Description

This program takes time input in seconds and counts down to zero.

It displays the remaining time in:

HH:MM:SS format

Once the timer reaches zero, it prints a completion message.

---

## 🛠 Concepts Used

- `import time`
- For loops
- `reversed(range())`
- Modulus operator `%`
- Integer division
- f-string formatting
- `time.sleep()` function

---

## 🧮 Logic Explanation

- `reversed(range(0, my_time))` counts backward from the entered time.
- Seconds are calculated using `% 60`
- Minutes are calculated using `(x / 60) % 60`
- Hours are calculated using `x / 3600`
- `time.sleep(1)` pauses execution for 1 second between each countdown step.

---

## ▶ How to Run

1. Open terminal inside the project folder.
2. Run:

python main.py

3. Enter time in seconds when prompted.

---

## 💡 Example

Enter the time in seconds : 10
00:00:10
00:00:09
00:00:08
...
00:00:01
!TIMES UP

---

## 🚀 Project Level

Beginner to Intermediate – Demonstrates time-based execution and formatted output using Python.