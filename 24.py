"""
Project Euler.net
Problem 24: Lexicographic permutations

"""

permutations = []

for i in range(10):
    for ii in range(10):
        for iii in range(10):
            for iiii in range(10):
                for j in range(10):
                    for jj in range(10):
                        for jjj in range(10):
                            for jjjj in range(10):
                                for k in range(10):
                                    for kk in range(10):
                                        if len(permutations) < 1000001:
                                         permutations.append([i,ii,iii,iiii,j,jj,jjj,jjjj,k,kk])
                                        else:
                                            break


print(permutations[-1])


print('done')