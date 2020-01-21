"""
Project Euler.net
Problem 4: Largest palindrome product
"""
import time

start = time.time()
palindromes = []
def palindromeCheck(number):
    """ Checks if a number is a palindrome"""
    if str(number) == str(number)[::-1]:
        palindromes.append(number)

n = 999

#squares
for i in range(900):
    product = (n-i)**2
    palindromeCheck(product)

#non squares
for i in range(900):
    for i in range(n):
        product = n * (n-i-1)
        palindromeCheck(product)
    n -= 1

end = time.time()
print(f'The answer is {max(palindromes)}')
print (f'Completion Time = {end-start}')



