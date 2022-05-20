# Python program that prints ascii table values between two integers

try:
    start = int(input("Enter the starting number: "))
    limit = int(input("Enter the limit number: "))

    if limit < start:
        raise ValueError

except ValueError:
    print("Invalid value(s)")
    quit()

# Prints a table containing the number in decimal, hexadecimal, binary, then the char it represents
print("DEC\t\tHEX\t\tBIN\t\tCHAR")
for i in range(start, limit + 1):
    print(f"{i}\t\t", end="")
    print(f"{hex(i)}\t\t", end="")
    print(f"{bin(i)}\t\t", end="")
    print(chr(i))
