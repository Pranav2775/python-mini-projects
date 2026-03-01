# ⏱ Styled Python Stopwatch (PyQt5 GUI)

A fully functional digital stopwatch built using Python and PyQt5 with millisecond precision and modern UI styling.

---

## 📌 Description

This application creates a real-time digital stopwatch that allows users to:

- Start the timer
- Stop (pause) the timer
- Reset the timer to zero

The stopwatch tracks time with millisecond precision and updates every 10 milliseconds.

---

## 🖥 Features

- Millisecond accuracy (10 ms interval updates)
- Modern dark theme UI
- Hover button effects
- Styled digital display
- Start / Stop / Reset controls
- Responsive layout design

---

## 🛠 Technologies Used

- Python
- PyQt5
- QTimer
- QLabel
- QPushButton
- QVBoxLayout & QHBoxLayout
- QFont
- Event-driven programming
- Object-Oriented Programming (OOP)

---

## 🧠 Program Structure

### Class: `Stopwatch(QWidget)`

Handles:

- Window setup
- UI design
- Button styling
- Timer management
- Time calculations

### Core Methods:

- `update_time()`  
  Calculates hours, minutes, seconds, and milliseconds.

- `start()`  
  Starts the timer with 10 ms interval.

- `stop()`  
  Stops the timer.

- `reset()`  
  Resets elapsed time to zero.

---

## ⏳ Time Format

The stopwatch displays time in:

```
HH:MM:SS:MS
```

Example:

```
00:01:25:340
```

---

## ▶ How to Run

### 1️⃣ Install PyQt5

```
pip install PyQt5
```

### 2️⃣ Run the Program

```
python main.py
```

A styled stopwatch window will appear.

---

## 🎨 UI Design

- Dark background
- Neon green time display
- Styled blue buttons
- Hover animation effect

---

## 🚀 Project Level

Intermediate to Advanced – Demonstrates GUI development, high-precision timing, event-driven architecture, and modern UI styling using PyQt5.