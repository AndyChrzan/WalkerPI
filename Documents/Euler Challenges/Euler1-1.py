threeorfive = []
def multiples(n):
    for n in xrange(1,n,1):
        if n%3 == 0:
            threeorfive.append(n)
        elif n%5 == 0:
            threeorfive.append(n)

multiples(1000)

print threeorfive
a = sum(threeorfive)
print"Sum: %s" %a
