"""
Project Euler.net
Problem 2: Even Fibonacci numbers
"""

def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()

evenNumbs = []
for fibNum in f:
    if fibNum % 2 == 0:
        evenNumbs.append(fibNum)
    if fibNum > 4000000:
        break

print(sum(evenNumbs))
