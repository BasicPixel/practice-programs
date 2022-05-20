# generator-args.py
# Python program that generates passwords with letters, digits, symbols.

import pyperclip
import string
import random
from sys import argv

if len(argv) < 2:
    print("Usage: python generator-args.py password_length")
    quit()

# Get password length from cl arguments
pw_length = int(argv[1])

characters = string.ascii_letters + string.digits
if '-s' in argv:
    characters += string.punctuation

password = ''
for i in range(pw_length):
    # Choose a random character from letters, digits, punctuation
    password += random.choice(characters)

# Show generated password, copy to clipboard
print(password)
pyperclip.copy(password)
print("Password copied to device clipboard.")
