"""
Project Euler.net
Problem 1: Multiples of 3 and 5
"""

multiples_of_3_or_5 = []

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples_of_3_or_5.append(i)

print(sum(multiples_of_3_or_5))
