not_prime = [1]
prime =[]


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

prifin(300)

    

