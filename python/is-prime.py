x = int(input("Enter a value for your number: "))


def check_prime_num(x):
    count = 0
    for i in range(2, x):
        if x % i == 0:
            count += 1
        elif x % i > 1:
            count = 0
    if count == 0:
        print("this is a prime number.")
    else:
        print("this is not a prime number.")


check_prime_num(x)
