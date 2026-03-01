# 🔐 Python Substitution Encryption Program

A command-line encryption and decryption program built using Python that uses a randomized substitution cipher.

---

## 📌 Description

This program implements a basic substitution cipher where:

- A shuffled key mapping is generated.
- Each character in the original text is replaced with a corresponding encrypted character.
- The program can also reverse the process (decrypt the text).

The encryption is based on randomly shuffled characters including:

- Letters (uppercase & lowercase)
- Digits
- Punctuation
- Space character

---

## 🔑 How It Works

1. A list of characters is created using:
   - `string.ascii_letters`
   - `string.digits`
   - `string.punctuation`
   - Space character

2. A copy of this list is shuffled randomly to create a key mapping.

3. During encryption:
   - Each character from the input text is replaced using the shuffled key.

4. During decryption:
   - The process is reversed using index matching.

---

## 🛠 Concepts Used

- `import random`
- `import string`
- Lists
- `.copy()` method
- `random.shuffle()`
- String iteration
- Index mapping (`list.index()`)
- Basic cryptography logic

---

## 🧠 Program Flow

- Generate character set
- Shuffle to create encryption key
- Encrypt user input
- Accept encrypted input
- Decrypt and display original message

---

## ▶ How to Run

1. Open terminal inside the project folder.
2. Run:

```
python main.py
```

3. Enter text to encrypt.
4. Enter encrypted text to decrypt.

---

## 💡 Example Output

```
write a text to excrypt : hello
your original text  : hello
your encrypted text : @#xP%

Enter a text to decrypt : @#xP%
your original text  : hello
```

(Note: Encrypted output will vary each run due to random key generation.)

---

## 🚀 Project Level

Intermediate – Demonstrates character mapping, random key generation, and substitution-based encryption logic using Python.