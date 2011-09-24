import math

def isPrime(n):
   return all(n%i!=0 for i in range(2,int(math.sqrt(n))+1))

def prob3():
    number = 600851475143
    return max(filter(isPrime, [i for i in range(2,int(math.sqrt(number))+1) if number % i == 0]))
print prob3()


max(filter(lambda n: all(n%i!=0 for i in range(2,n)), [i for i in range(2,600851475143) if number % i == 0]))
