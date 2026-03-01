# 🧠 Python Quiz Game

A command-line quiz game built using Python that tests general knowledge and calculates the final score.

---

## 📌 Description

This program presents multiple-choice questions to the user.

For each question:
- Four options (A, B, C, D) are displayed
- The user selects an answer
- The program checks correctness
- Score is updated accordingly

At the end, the program:
- Displays correct answers
- Displays user guesses
- Calculates final percentage score

---

## 🛠 Concepts Used

- Tuples
- Nested tuples
- For loops
- Conditional statements (`if-else`)
- List storage (`append()`)
- Index tracking
- Score calculation
- String formatting
- Percentage calculation

---

## 🧠 Program Logic

1. Questions are stored in a tuple.
2. Options are stored as nested tuples.
3. Correct answers are stored in a separate tuple.
4. The program loops through each question.
5. User input is converted to uppercase using `.upper()`.
6. Score increases for each correct answer.
7. After all questions:
   - Correct answers are displayed.
   - User guesses are displayed.
   - Final score percentage is calculated.

---

## ▶ How to Run

1. Open terminal inside the project folder.
2. Run:

```
python main.py
```

3. Enter your answers (A, B, C, or D).

---

## 💡 Example Output

```
-------------------------------------
how many elements are in periodic table ?:
A.116
B.117
C.118
D.119
enter(A,B,C,D) : C
correct
```

Final result:

```
answers :  C D A A B
guesses :  C D A B B
your score is: 80%
```

---

## 🚀 Project Level

Intermediate Beginner – Demonstrates structured data handling, indexing, score tracking, and percentage calculation in Python.