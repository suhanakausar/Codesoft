import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

print("Include:")
print("1. Letters")
print("2. Digits")
print("3. Symbols")

use_letters = input("Include letters? (y/n): ")
use_digits = input("Include digits? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

characters = ""

if use_letters.lower() == 'y':
    characters += string.ascii_letters
if use_digits.lower() == 'y':
    characters += string.digits
if use_symbols.lower() == 'y':
    characters += string.punctuation

if characters == "":
    print("Please select at least one option!")
else:
    password = "".join(random.choice(characters) for i in range(length))
    print("Generated Password:", password)