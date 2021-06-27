###############################################################################
# Project Euler Problem 1
# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
###############################################################################

def multiples_of(a, b, limit):
    total = 0
    for i in range(limit):
        if (i % a == 0) or (i % b == 0):
            total += i
    return total


print(multiples_of(3, 5, 1000))
