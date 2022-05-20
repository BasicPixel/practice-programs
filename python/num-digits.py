def countDigits(n):
    return len(list(str(n)))


number = int(input("Enter a number: "))

print(f"The integer {number} has {countDigits(number)} digits")
