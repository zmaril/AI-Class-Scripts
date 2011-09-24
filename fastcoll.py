import time

ulam = { 1: 1 }
def collatz(n):
    if not n in ulam:
        ulam[n] = collatz(3*n+1 if n%2 else n/2) + 1
    return ulam[n]

max = (0,0)
limit = raw_input("Enter the Max limit: ")
limit = int(limit)
index = raw_input("Enter the starting Number: ")
index = int(index)
#limit = 200
start = time.strftime('%s')
if index % 2 == 0:
    for i in range(index+3,limit,2):
        length = collatz(i)
        if length > max[1]: max = (i,length)
else:
    for i in range(index,limit,2):
        length = collatz(i)
        if length > max[1]: max = (i,length)

end = time.strftime('%s')
time = int(end) - int(start)
print "(Number, Chain Length) =", max
print "Time to execute the algorithm =", time ,"Second(s)"
