import math
from math import sqrt

factor = []
primefactor = []

n = 600851475143

for i in xrange(1,int(sqrt(n)),1):
    if n%i == 0:
        factor.append(i)
print factor

def prime_check(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i,isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

for i in factor:
    if prime_check(i) == True:
        primefactor.append(i)
        
print primefactor
