"""
Project Euler.net
Problem 25: 1000-digit Fibonacci number
"""

def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()

for i,fibNum in enumerate(f, start=0):
    if len(str(fibNum)) ==1000:
        print(i)
        break

print('done')