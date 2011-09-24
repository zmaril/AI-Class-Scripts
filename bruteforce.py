def next(n): # computes next term in the sequence
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1

maxnum = 1
num = 0
for i in range(2,1000000):
    rem = next(i)
    length = 1
    while(rem != 1):
        rem = next(rem)
        length += 1
    if length > maxnum:
        maxnum = length
        num = i
print num, maxnum

