#!/usr/bin/python
# sha256_500k.py
# calcolo del tempo per 500000 sha256
# 
# by Nanni Bassetti - http://www.nannibassetti.com - digitfor@gmail.com

import hashlib
i=0
from datetime import datetime

tstart = datetime.now()
print "tempo iniziale:", tstart
while i<500000: # qui potete cambiare i cicli per vedere come aumentano/diminuiscono i tempi
	i=i+1
	hash_pw_salt = hashlib.sha256('pippo'+unicode(i))
	hex_value = hash_pw_salt.hexdigest()
	#print(hex_value)
tend = datetime.now()
print "tempo finale : ", tend
print "tempo totale: ",tend - tstart
print 'fine'     
print(hex_value)  
