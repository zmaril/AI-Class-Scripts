import math

##Correct
def prob1():
    return sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])

##Correct
def prob2():
    a= 1
    b= 2 
    thusfar = 0
    while a<4000000:
        if a% 2 == 0:
            thusfar += a
        temp = b
        b +=a 
        a = temp
    return thusfar

##Correct  
def prob3():
     n = 600851475143
     i=2;
     while i<math.sqrt(n):
         if n % i == 0:
             n = n /i
         else:
             i +=1
     return n

##Correct
def prob4():
    pals =[x*y 
           for x in range(100,1000) 
           for y in range(100,1000) 
           if x*y == int(str(x*y)[::-1])
           ]
    pals.sort()
    return pals[-1]

##Correct
def prob5(n):
    if n ==1:
        return 1
    d = prob5(n-1)
    dumbluck = 0
    found = False
    numbers = range(1,n+1)
    while not found:
        dumbluck += d
        if all(dumbluck%number==0 for number in numbers):
            found=True

    return dumbluck

#Other verision pointed out by charles
def prob5b():
    return reduce(lcm,range(1,21))

# the function to calculate the GCD
def gcd(num1, num2):
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result

    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result

    else:
        result = num1*num2/num1
        return result

# the function to calculate the LCM
def lcm(num1, num2):
    result = num1*num2/gcd(num1,num2)
    return result

##Correct. There is a way to compute this directly given a n.
def prob6():
    sumsquare = sum([math.pow(x,2) for x in range(101)]) 
    squaresum = math.pow(sum([x for x in range(101)]),2)
    return squaresum-sumsquare

##Correct
def prob7():
    count = 2
    suspect = 3
    while count < 6:
        suspect += 2##Watch the order of things. 
        if isPrime(suspect):
            count += 1
    return suspect

def isPrime(n):
    if n==0: return False
    if n==1: return False
    if n==2: return True
    bound = int(math.ceil(math.sqrt(n)))+1
    belows =  range(bound)
    if 0 in belows: belows.remove(0)
    if 1 in belows: belows.remove(1)
    return not any(n % x == 0 for x in belows)

##Correct
def prob8():
    digits ="73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"
    greatest = 1
    for i in range(len(digits)):
        current = reduce(lambda a,b:a*b, map(lambda x: int(x), digits[i:i+5]))
        if current > greatest:
            greatest=current
    return greatest

##Correct
def prob9():
    return [a*b*c 
            for c in range(1000) 
            for b in range(c) 
            for a in range(b) 
            if a+b+c==1000 and math.pow(a,2)+math.pow(b,2)==math.pow(c,2)]

##Correct but slow
def prob10():
    raws = [2]
    raws.extend(range(3,2000000,2))
    return sum(filter(lambda x: isPrime(x), raws))

##Fast attempt at prime wheel factorization. 
def prob10b():
    print 2+3+sum(wheelPrimes(2000000))

##Starts at 5 and then works its way up the chain up to, but not including, n. Uses wheel factorization, with a period of 30 (2*3*5). So, it looks at 5,7,11,13,17,19,23,29,31,35 and then repeats the same pattern over again. Too lazy to try to figure out a larger wheel right now. Probably going to program a computer to do it later. fv
def wheelPrimes(n):
    wheelList = [2,4,2,4,2,4,6,2,4]
    wheelIndex = 0
    counter = 5
    primes = []
    while counter<n:
        if isPrime(counter):
            primes.append(counter)
        counter += wheelList[wheelIndex]
        wheelIndex = (wheelIndex + 1)% len(wheelList)
    return primes

##Test to see if the things are working correctly in comparsion. zip is a neat function that takes two lists and produces a list of tupes of the corresponding elements. Filter takes a function that returns true or false and a list, then removes the elements from the list which don't return true. 
def test():                              
    return zip(wheelPrimes(2000), filter(isPrime,range(5,2000,2)))
    
