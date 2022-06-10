# https://dev.to/atebarhaider/sieve-of-eratosthenes-algorithm-4ol
# This program is NOT complete yet.

n = int(input("Enter a whole number: "))

# 1. To find out all primes under n, generate a list of all integers from 2 to n.
primes = range(2, n + 1)

# 2. Start with a smallest prime number, i.e. p = 2
p = 2

# 3. Mark all the multiples of p which are less than n as composite. To do this, we will mark the number as 0. (Do not mark p itself as composite.)
# while p * p <= n:


# 4. Assign the value of p to the next non-zero number in the list which is greater than p.

# 5. Repeat the process until p*p ≤ n
