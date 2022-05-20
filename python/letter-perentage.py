text = input("Text: ")
letter_dict = {}


def get_percentage(letter):
    """Calculates the percentage of a letter in the text"""
    return 100 * float(letter_dict[letter]) / float(len(text))


# Loop over letters in the text, incrementing recurrence count each time the letter is seen
for letter in text:
    if letter not in letter_dict:
        letter_dict[letter] = 1
    else:
        letter_dict[letter] += 1

# Sorts the dictionary by recurrence count, then prints the letter with its percentage (limited to 4 decimal places)
for letter in sorted(letter_dict, key=letter_dict.get, reverse=True):
    print(f"{letter}: {get_percentage(letter):.4f}%")
