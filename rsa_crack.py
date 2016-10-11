#!/usr/bin/python2
# RSA_CRACK.py
# Cracking RSA key - finding the two prime numbers those make the key
# finding the private exponent
# this is only for didactic purposes.
# by Nanni Bassetti - http://www.nannibassetti.com - digitfor@gmail.com

import random, math

# n is the key
n = 824296325825751113
# e is the public exponent
e = 65537
q=int(math.sqrt(n))

# factorize
r1 = 1
while r1 != 0 :
	q = q+1
#	print "q=",q
	r1 = n % q
	p = n/q

print 'p =',p,'q =',q
# finding d (private exponent)
k=0
f=(p-1)*(q-1)
r2=1
while r2 != 0 : # devo trovare (e*d) -1 / f = 1  quindi (e*d)-1 = f quindi e*d=f+1 quindi d=(f+1)/e
# pertanto devo trovare un numero k tra 1 ed e, che moltiplicato per f e sommato ad 1 renda r2 divisibile per e
	k=random.randint(1,e)
	r2=(f*k+1) % e
#print 'k=',k
d=(f*k+1) / e
print 'd=',d 

