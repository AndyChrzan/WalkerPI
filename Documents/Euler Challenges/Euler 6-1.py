sumofsquarelist = []
squareofsumlist = []

def sumofsquares(n):
    for i in xrange(1,n+1,1):
        sumofsquarelist.append(i**2)

def squareofsum(n):
    for i in xrange(1,n+1,1):
        squareofsumlist.append(i)
        
sumofsquares(100)
squareofsum(100)

a = sum(squareofsumlist)
b = sum(sumofsquarelist)
c = a**2 - b

print sumofsquarelist
print squareofsumlist
print "sum of naturals: %s" %a
print "sum of naturals squared: %s" %a**2
print "sum of sum of squared naturals: %s" %b
print "difference between sum of naturals squared and squared sum of naturals:%s" %c

