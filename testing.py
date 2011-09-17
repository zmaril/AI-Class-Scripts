def gcd(n,j):
    if n==j:
        return n
    elif n>j:
        return gcd(n-j,j)
    else:
        return gcd(j,j-n)

def newgcd(n,j):
    a= n
    b= j
    while a != b:
        if a >b:
            a = a -b
        else:
            b = b -a
    return a

def unique(li):
    clean = li 
    dups = [x for x  in li if li.count(x) != 1]
    unis = [
def gcdlist(n):
    elements = range(n)
    elements.remove(0)
    return unique([newgcd(n,i) for i in elements])

print gcdlist(12)
