#!/usr/bin/python
# by Nanni Bassetti - http://www.nannibassetti.com - digitfor@gmail.com

import math
def main():
	
	P=1
	for i in range(1,23) :
		P=P*(365-i)/float(365) # prob. che due persone NON abbiano il compleanno nella stessa data
		P1=float((1-P))*100 # prob. complementare, ossia che due persone abbiano il compleanno nella stessa data
		print P," ",i
	print 'P: ',P1,"%"


main()
