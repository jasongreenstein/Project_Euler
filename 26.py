"""""
Project Euler.net
Problem 26: Reciprocal cycles
"""

import decimal

decimal.getcontext().prec = 1000

D = decimal.Decimal


for i in range(3,1001):
    unitFraction = str(D(1)/D(i))
    for ii in range(500,7,-1):
        first = unitFraction[2:ii+2]
        second = unitFraction[ii+2:(ii*2)+2]
        if first == second and unitFraction[2]!=unitFraction[3]:
            print(first)
            print(i)
            break
    break

print('done')
