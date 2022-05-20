# Random words API: https://random-word-api.herokuapp.com/word?number=[count]

import requests
import os

r = requests.get("https://random-word-api.herokuapp.com/word?number=1")

word_to_guess = r.json()[0]

print(" Python Hangman ".center(80, "="))

difficulty = int(
    input("Difficulty: (1:easy, 2:med, 3:hard, 4:impossible):  "))

# Sets attempt count based on difficulty
match difficulty:
    case 1:
        attempts = len(word_to_guess) + 1
    case 3:
        attempts = len(word_to_guess) - 1
    case 4:
        attempts = 1
    case _:
        attempts = len(word_to_guess)

if attempts > 9:
    attempts = 9

correct_letters = []
incorrect_letters = []

word_template = "_"*len(word_to_guess)


def regenerate_template():
    """Regenerates word template based on the guessed letters"""
    global word_template

    new_template = ""

    for letter in word_to_guess:
        if letter in correct_letters:
            new_template += letter
        else:
            new_template += "_"

    word_template = new_template


def check_letter(guessed_letter):
    """Appends a guessed letter to correct / incorrect letter lists"""
    global attempts

    if guessed_letter in word_to_guess:
        correct_letters.append(guessed_letter)

    else:
        incorrect_letters.append(guessed_letter)
        attempts -= 1

    regenerate_template()


while True:
    # Clears the console by a system call
    # Uses the 'cls' command on windows, 'clear' otherwise
    os.system('cls' if os.name == 'nt' else 'clear')

    # Finish the game if attempts reach zero or if the word is guessed correctly
    if word_template == word_to_guess or attempts == 0:
        break

    print(word_template)

    if incorrect_letters:
        print("Letters already guessed: ", *incorrect_letters)

    print(f"Attempts left: {attempts}")

    letter = ""

    while letter in correct_letters or letter in incorrect_letters or not letter.isalpha() or len(letter) > 1:
        letter = input("Guess a letter: ")

    check_letter(letter)

print("Congratulations, You Win !" if attempts > 0 else "GAME OVER !")

print(f"The word was: {word_to_guess}")
