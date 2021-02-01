def prime_check(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i,isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False
    
if prime_check(3) == True:
    print "it is prime!"
else:
    print "it is NOT prime."

