"""
Project Euler.net
Problem 7: 10001st prime
"""
import math
def primeChecker(n):
    """"returns True if n is prime, False if otherwise"""
    isPrime = True
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            isPrime = False
            break

    if isPrime:
        return True

counter = 0
number = 1
while counter != 10001:
    number +=2               # only odd numbers can be prime
    if primeChecker(number):
        counter += 1

print(number)