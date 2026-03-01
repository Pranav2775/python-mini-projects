# ⏰ Python Alarm Clock with Sound

A real-time command-line alarm clock built using Python that plays a sound when the alarm time is reached.

---

## 📌 Description

This program allows the user to:

- Set an alarm time in HH:MM:SS format
- Continuously monitor the system clock
- Play an alarm sound when the set time is reached

The alarm uses the `pygame` library to play an MP3 file when triggered.

---

## 🔊 Features

- Real-time system clock tracking
- Sound alert using `pygame`
- Automatic stop after alarm sound finishes
- Continuous time display in terminal

---

## 🛠 Concepts Used

- `import datetime`
- `import time`
- `import pygame`
- `datetime.datetime.now()`
- `.strftime()` for time formatting
- Infinite loop with condition checking
- Audio playback using `pygame.mixer`
- External file handling (MP3)

---

## 🧠 Program Logic

1. The user enters an alarm time (HH:MM:SS).
2. The program continuously checks the current system time.
3. When the current time matches the alarm time:
   - A wake-up message is printed.
   - The alarm sound (`alarm.mp3`) is played.
4. The program waits until the sound finishes before stopping.

---

## 📂 Requirements

- Python installed
- `pygame` library installed
- An audio file named `alarm.mp3` in the same directory

Install pygame using:

```
pip install pygame
```

---

## ▶ How to Run

1. Place an `alarm.mp3` file in the project folder.
2. Open terminal inside the folder.
3. Run:

```
python main.py
```

4. Enter alarm time in HH:MM:SS format.

---

## 💡 Example

```
Enter alarm time (HH:MM:SS): 07:00:00
Alarm set for 07:00:00
Current time: 06:59:58
Current time: 06:59:59
Current time: 07:00:00

WAKE UP! ⏰
```

---

## 🚀 Project Level

Intermediate – Demonstrates real-time clock monitoring, external library integration, and multimedia handling using Python.