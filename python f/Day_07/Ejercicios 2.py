#sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

AB = A.union(B)                                                                             #1, 5
BA = B.union(A)

print(A.intersection(B))                                                                    #2

print(A.issubset(B))                                                                        #3

print(A.isdisjoint(B))                                                                      #4

print(A.symmetric_difference(B))                                                            #5

del A                                                                                       #6
del B