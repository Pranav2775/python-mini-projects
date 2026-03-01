import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

print(f"chars : {chars}")
print(f"keys  : {keys}")

#ENCRYPT MESSAGE

plain_text = input("write a text to excrypt : ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"your original text  : {plain_text}")
print(f"your encrypted text : {cipher_text}")

# Decrypt text

cipher_text = input("Enter a text to decrypt : ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"your encrypted text : {cipher_text}")
print(f"your original text  : {plain_text}")