"""
Project Euler.net
Problem 3: Largest prime factor
"""
import math

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i ==0:
            return False
    return True

prime_numbers = []
for number in range(0,600851475143):
    if isPrime(number) == True:
        prime_numbers.append(number)

print(prime_numbers[-1])
