# 🧮 Simple Python Calculator

A beginner-friendly command-line calculator that performs basic arithmetic operations using Python.  
This project is part of my **Python Mini Projects** series to strengthen foundational programming skills.

---

## ✨ Features
- ➕ Addition  
- ➖ Subtraction  
- ✖ Multiplication  
- ➗ Division (with zero-division error protection)

---

## 📦 Project Structure

02-calculator-program/
│
├── calculator.py # Main calculator program
└── README.md # Project documentation

yaml
Copy code

---

## ▶️ How to Run the Program

Open a terminal and run the following:

```bash
cd "D:\Python Projects\python-mini-projects\02-calculator-program"
python calculator.py
Make sure Python is installed and added to PATH.

## 📝 User Input Format
The program will ask you for:
Operator → one of + - * /
First number
Second number

#📌 Example
mathematical
Copy code
Enter the operator (+,-,*,/) : *
Enter the value of num 1 : 5
Enter the value of num 2 : 6
30.0

#🚫 Error Handling
If the user enters / and second number is 0 → shows friendly error:

vbnet
Copy code
Error : cannot divide by zero
If the operator is invalid → shows:
cpp
Copy code
Invalid operator

#📚 What I Learned
Working with conditional statements (if-elif-else)
Taking user input using input()
Type conversion using float()
Basic arithmetic operations in Python

#📌 Upcoming Improvements
Support for multiple calculations in one run
GUI version using Tkinter
History of operations
More operators (power, modulus, etc.)
