"""
Project Euler.net
Problem 22: Names scores
"""
import csv

file = open(r"C:\Users\Jason_Greenstein\Documents\Project Euler\22.txt", 'r')

names = file.read().split('","')

names[0] = 'MARY'
names[-1] = 'ALONSO'

# sort list of names
names.sort()

letters = ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P',
           'Q','R','S','T','U','V','W','X','Y','Z']

sumScore = 0

for name in names:
    alphValue = 0
    for letter in name:
            alphValue = (alphValue + letters.index(letter) + 1)

    alphValue = alphValue*(names.index(name) + 1)
    sumScore = sumScore + alphValue


file.close()

print(sumScore)
print("done")