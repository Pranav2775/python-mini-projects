# ⚖️ Python Weight Converter

A simple and beginner-friendly Python program that converts weight between kilograms (kg) and pounds (lbs).  
This project is part of my **Python Mini Projects** collection.

---

## ✨ Features
- Convert **kg → lbs**
- Convert **lbs → kg**
- Validates incorrect unit input

---

## 📁 Project Structure

03-weight-converter/
│
├── weight_converter.py # Main conversion script
└── README.md # Project documentation

yaml
Copy code

---

## ▶️ How to Run the Program

Open your terminal and execute:

```bash
cd "D:\Python Projects\python-mini-projects\03-weight-converter"
python weight_converter.py
📝 How It Works
1️⃣ Enter your weight
2️⃣ Enter the unit (kg or lbs)
3️⃣ Program converts and displays the result

#📌 Example Output
csharp
Copy code
Enter your weight : 60
enter the units (kg or lbs) : kg
your weight is 132.3 lbs
csharp
Copy code
Enter your weight : 150
enter the units (kg or lbs) : lbs
your weight is 68.02721088435375 kg

#🚫 Error Handling
If the user enters anything other than kg or lbs:
csharp
Copy code
the unit is invalid

#📚 What I Learned
Floating point number conversion
Conditional logic (if-elif-else)
Basic input validation
Unit conversion formulas

#🚀 Future Enhancements
Round numbers to 2 decimal places
Support more units (grams, tons, stones)
Add a loop so multiple conversions can be done at once
GUI version using Tkinter