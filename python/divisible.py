# Checks if two numbers are divisible

x = int(input("Insert the numerator: "))
y = int(input("Insert the denominator: "))

print(f"{x} is divisible by {y}") if x % y == 0 else print(
    f"{x} not divisible by {y}")
