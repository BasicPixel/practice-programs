# division.py
# Performs division on two numbers without using the / operator

# Natural -> Natural
# Performs division on two given numbers

# def divide(a, b): return 0 # stub

def divide(a, b):
    quotient = 0
    remainder = a

    if a < b:
        return (0, a)

    while (not remainder < b):
        quotient += 1
        remainder -= b

    return quotient + remainder / b


print(divide(4.5, 2))
print(divide(8, 2))
print(divide(8.5, 4))
print(divide(14, 3))
