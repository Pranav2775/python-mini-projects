# 🕒 Python Digital Clock (PyQt5 GUI)

A real-time digital clock application built using Python and PyQt5.

---

## 📌 Description

This program creates a graphical digital clock that:

- Displays the current system time
- Updates automatically every second
- Uses a styled GUI interface
- Shows time in 12-hour format with AM/PM

The clock runs continuously until the window is closed.

---

## 🖥 GUI Features

- Black background
- Lime green digital-style text
- Large bold font
- Center-aligned time display
- Real-time updating using QTimer

---

## 🛠 Technologies Used

- Python
- PyQt5
- QTime
- QTimer
- QWidget
- QLabel
- QHBoxLayout
- QFont

---

## 🧠 Program Structure

### Class: `DigitalClock(QWidget)`

- Creates main application window
- Configures layout and styling
- Initializes timer
- Updates time every second

### Method: `update_time()`

- Fetches current system time
- Formats time using `"hh:mm:ss AP"`
- Updates label display

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

A digital clock window will open.

---

## 💡 Display Example

```
08:45:12 PM
```

(Updates every second automatically)

---

## 🚀 Project Level

Intermediate to Advanced – Demonstrates GUI development, object-oriented programming, event-driven architecture, and real-time updates using PyQt5.