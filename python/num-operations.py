# Python program that detects several props of an integer and prints them

def isPrime(n):
    # https://stackoverflow.com/q/15285534/14900882

    if n < 2:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True


def isPositive(n):
    if n > 0:
        return True
    elif n < 0:
        return False
    return 0


def isOdd(n):
    if n % 2 == 1:
        return True
    return False


number = int(input("Enter a number: "))

print("Number is prime") if isPrime(number) else print("Number is not prime")
print("Number is positive") if isPositive(number) else print(
    "Number is negative") if isPositive(number) == False else print("0")
print("Number is odd") if isOdd(number) else print("Number is even")
