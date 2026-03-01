# 🏦 Python Banking Program

A menu-driven command-line banking system built using Python.

---

## 📌 Description

This program simulates a basic banking system where users can:

- Check account balance
- Deposit money
- Withdraw money
- Exit the system

The program maintains account balance and ensures proper validation for deposits and withdrawals.

---

## 🛠 Concepts Used

- Functions
- Return values
- Parameter passing
- While loops
- Conditional statements (`if-elif-else`)
- State management using variables
- Input validation
- `if __name__ == "__main__"` execution guard
- f-string formatting

---

## 🧠 Program Structure

### Functions Included:

- `show_balance(balance)`  
  Displays the current account balance.

- `deposit()`  
  Accepts deposit amount and validates input.

- `withdraw(balance)`  
  Checks for sufficient funds before withdrawing.

- `main()`  
  Controls the program flow using a menu-driven loop.

---

## 🔐 Validation Rules

- Deposit amount cannot be negative.
- Withdrawal amount must be greater than 0.
- Withdrawal cannot exceed current balance.

---

## ▶ How to Run

1. Open terminal inside the project folder.
2. Run:

```
python main.py
```

3. Select options from the displayed menu.

---

## 💡 Example Output

```
1.show balance
2.deposit
3.withdraw
4.exit

enter your choice (1-4): 2
enter the amount u like to deposit : 500

1.show balance
2.deposit
3.withdraw
4.exit

enter your choice (1-4): 1
your total balance is $500.00
```

---

## 🚀 Project Level

Intermediate Beginner – Demonstrates function-based structure, state management, and financial transaction logic using Python.