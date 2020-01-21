"""
Project Euler.net
Problem 5: Smallest multiple
"""


for n in range(100000000,1000000000):
    for i in range(2,21):
        if n%i == 0 and i !=20:
            continue
        elif n%i == 0 and i ==20:
            print(f'The answer is {n}')
            break
        else:
            break

