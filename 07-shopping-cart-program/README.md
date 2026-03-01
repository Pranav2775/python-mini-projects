# 🛒 Python Shopping Cart Program

A simple command-line shopping cart program built using Python.

---

## 📌 Description

This program allows users to:

- Enter food items they want to purchase
- Enter the price for each item
- Quit the program by typing `q`
- View all selected items
- See the total bill amount

The program stores food names and prices in separate lists and calculates the total cost at the end.

---

## 🛠 Concepts Used

- Lists (`append()`)
- While loops
- Conditional statements (`if-else`)
- User input handling
- String methods (`lower()`)
- Accumulator pattern for calculating total
- f-string formatting

---

## 🧠 Program Logic

1. Two empty lists are created:
   - `foods` → stores item names
   - `prices` → stores item prices
2. The user keeps entering food items until they type `q`.
3. Each food and its price are added to respective lists.
4. The program prints all selected items.
5. It calculates the total by adding all prices.
6. The final total amount is displayed.

---

## ▶ How to Run

1. Open terminal inside the project folder.
2. Run:

```
python main.py
```

3. Follow the on-screen prompts.

---

## 💡 Example

```
Enter a food you like to buy (q to quit) : Burger
Enter the price of Burger : $50
Enter a food you like to buy (q to quit) : Pizza
Enter the price of Pizza : $100
Enter a food you like to buy (q to quit) : q

-----YOUR CART-----
Burger
Pizza

your total is: 150
```
---

## 🚀 Project Level

Beginner to Intermediate – Demonstrates list handling and basic cart simulation logic in Python.