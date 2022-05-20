word = "pixel"
guess = ""
count = 0

while guess != word and count < 3:
    guess = input("Enter your guess: ")
    count += 1

if guess != word:
    print("You lose")
else:
    print("Correct")
