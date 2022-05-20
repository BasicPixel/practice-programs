# generator.py
# Python program that generates random passwords with different options.
# Options:
# - Password length.
# - Include uppercase.
# - Include lowercase.
# - Include digits.
# - Include symbols.

import pyperclip
import string
import random


def prompt_option(prompt_text):
    '''
    Prompts user for yes / no answer to a password generator option.
    '''
    answer = input(prompt_text)
    if answer.lower() in 'yes':
        return True
    elif answer.lower() in 'no':
        return False
    else:
        print(f"Invalid answer: {answer}.")
        return prompt_option(prompt_text)


# 1. Get password generator options from user

# 1.1 Prompt user for password length
try:
    pw_length = int(input("Password Length: "))
except ValueError:
    print("Password length must be an integer.")
    quit()

# 1.2 Prompt user for each option and store value
include_uppercase = prompt_option('Include uppercase? [y/n]: ')
include_lowercase = prompt_option('Include lowercase? [y/n]: ')
include_digits = prompt_option('Include digits? [y/n]: ')
include_symbols = prompt_option('Include symbols? [y/n]: ')

# If all options are false, print error message and quit
if not any([include_uppercase, include_lowercase, include_digits, include_symbols]):
    print("Error: password must include at least one of the options above.")
    quit()


# 2. Generate Password

# String stores all characters we can choose from, depending on the options provided
all_chars = ''

if include_uppercase:
    all_chars += string.ascii_uppercase
if include_lowercase:
    all_chars += string.ascii_lowercase
if include_digits:
    all_chars += string.digits
if include_symbols:
    all_chars += string.punctuation

# Initialize password string
password = ''
for i in range(pw_length):
    password += random.choice(all_chars)

# 3. Show generated password, copy to clipboard
print(password)
pyperclip.copy(password)
print("Password successfully copied to clipboard.")
