"""
Project Euler.net
Problem 23: Non-abundant sums

Answer = 4179871
"""

import math

def listFactors(number):
    """returns a list of all factors of a number"""
    factors = []
    for i in range(1,int(math.sqrt(number)) +1):
        if number%i == 0:
            factors.append(i)
            factors.append(int(number/i))

    del factors[factors.index(number)]
    return set(factors)



def abundant(number):
    """returns true and the number if the number is abundant"""
    sumFactors = sum(listFactors(number))
    if sumFactors > number:
        return True, number
    else:
        return False, number

# create a list of all abundant numbers
abundantNumbers = []
for i in range(1,28124):
    if abundant(i)[0]:
        abundantNumbers.append(i)

answerList = []

for i in range(1,28124):
    if i%2000 == 0:
        print(i)
    differnceList = []
    for ii in range(len(abundantNumbers)):
        if i in answerList:
            break
        else:
            difference = i-abundantNumbers[ii]
            if difference <= 0:
                break
            else:
                if not abundant(difference)[0]:
                    pass
                else:
                    differnceList.append('a')
    if len(differnceList)==0:
        answerList.append(i)




print(sum(answerList))
print('done')