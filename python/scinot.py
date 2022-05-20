# scinot.py
# A program to convert a number from standard notation to scientific notation

try:
    number = float(input("Number to be converted: "))
except ValueError:
    print("Invalid number.")
    quit()


def convert(n):
    power = 0
    if n < 1:
        while n < 1:
            n *= 10
            power -= 1

    elif n > 10:
        while n > 10:
            n /= 10
            power += 1

    return f"{n:.4f} * 10^{power}"


print(convert(number))
