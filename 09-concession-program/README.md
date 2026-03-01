# 🍕 Python Concession Stand Program

A command-line concession stand ordering system built using Python.

---

## 📌 Description

This program simulates a simple concession stand where users can:

- View a menu with item prices
- Select multiple food items
- Add items to their cart
- Quit by typing `q`
- View their final order
- See the total bill amount

The program uses a dictionary to store menu items and their prices.

---

## 🛠 Concepts Used

- Dictionaries (`dict`)
- Dictionary iteration (`.items()`)
- Dictionary value retrieval (`.get()`)
- Lists
- While loops
- Conditional statements
- Accumulator pattern for calculating total
- String formatting
- f-strings

---

## 🧠 Program Logic

1. A dictionary named `menu` stores food items and their prices.
2. The program displays the full menu.
3. The user selects items until they type `q`.
4. Each valid item is added to the cart list.
5. The total is calculated by retrieving prices from the dictionary.
6. The final order and total bill are displayed.

---

## ▶ How to Run

1. Open terminal inside the project folder.
2. Run:

```
python main.py
```

3. Select items from the menu.
4. Type `q` to finish ordering.

---

## 💡 Example Output

```
--------MENU---------
pizza      : $3.00
nachos     : $4.50
popcorn    : $6.00
fries      : $2.50
chips      : $1.00
pretzel    : $3.50
soda       : $3.00
lemonade   : $4.25
---------------------

select an item (q to quit) : pizza
select an item (q to quit) : soda
select an item (q to quit) : q

-----------Your Order------------
pizza soda
your total is : 6.00
```

---

## 🚀 Project Level

Intermediate Beginner – Demonstrates dictionary usage, data retrieval, and real-world ordering system simulation in Python.