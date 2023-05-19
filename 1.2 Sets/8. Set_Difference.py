# Using "-" symbol
A = {1, 2, 3, 4, 5, 6}
B = {1, 3, 5, 7, 9}
print(A-B)    # This means in A not in B


# Using "difference()" method
C = {2, 4, 6, 8}
print(A.difference(C))      # This means in A not in C

set1 = set([4, 5, (6, 7)])

set1.update([5, 2, 6])

check1 = 2 in set1

check2 = 6 in set1

print(check1 and check2)