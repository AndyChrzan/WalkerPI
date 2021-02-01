not_prime = [1]
prime =[]
Trunk_PrimesL = []
Trunk = []

def prifin(n):
    for i in xrange(2, n+1):
        if i <= 40000:
            if i not in not_prime:
                prime.append(i)
            for j in xrange(i*i,n+1,i):
                    not_prime.append(j)
        if i > 40000:
            if i not in not_prime:
                prime.append(i)
    print prime


def trunkpriL(n): 
    for k in prime:
        if k >= 11:
            M = str(k)[1:]
            if int(M) in prime and int(M) < 11:
                Trunk_PrimesL.append(k)
            while int(M) > 11 and int(M) in prime:
                M = str(M)[1:]
                if int(M) in prime and int(M) <= 11:
                        Trunk_PrimesL.append(k)
    print Trunk_PrimesL
                

def trunkpriR(n):
    for p in Trunk_PrimesL:
        if p >= 11:
            P = str(p)[:-1]
            if int(P) in prime and int(P) < 11:
                Trunk.append(p)
            while int(P) > 11 and int(P) in prime:
                P = str(P)[:-1]
                if int(P) in prime and int(P) < 11:
                        Trunk.append(p)
            

trunkpriR(trunkpriL(prifin(4000)))

print Trunk
a = sum (Trunk)
print "Sum of Trunkable Primes Found: %s" %a
print "Number of Trunkable Primes Found: %s" %len(Trunk)
                
        
    

