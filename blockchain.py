#!/usr/bin/python
# blockchain.py
# Simulatore di blockchain
# programma ad uso didattico - only for didactic using
# il programma serve solo a capire i principi base della blockchain - the program intents only to explain the basic rules of blockchain
# by Nanni Bassetti - http://www.nannibassetti.com - digitfor@gmail.com

import hashlib
import time

def main():
	global genesis,p,s,t,q,indx,phash,t0,t1,t2,t3,t4,tb,vb,block,timestamp
	
	genesis=0
	t0 = int(time.time())
	g = "ciao sono il contenuto del blocco di generazione"
	p = raw_input('Inserisci valore del primo blocco:')
	t1 = int(time.time())
	s = raw_input('Inserisci valore del secondo blocco:')
	t2 = int(time.time())
	t = raw_input('Inserisci valore del terzo blocco:')
	t3 = int(time.time())
	q = raw_input('Inserisci valore del quarto blocco:')
	t4 = int(time.time())
	vb = [g,p,s,t,q]
	tb = [t0,t1,t2,t3,t4]
	phash = [0,1,2,3,4]
	block = [0,1,2,3,4]
	crea_blockchain()
	
def crea_blockchain():
	indx=-1
	
	while indx <= len(vb)-2: 
		indx = indx + 1
		timestamp = tb[indx]
		block[indx]=hashlib.sha1(unicode(indx)+unicode(phash[indx])+unicode(timestamp)+unicode(vb[indx])).hexdigest()
		phash[indx] = 0
		if indx > 0:
			phash[indx] = block[indx-1]
		print "Blocco"+unicode(indx)+": "
		print "		Indice:"+unicode(indx)
		print "		Timestamp: "+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timestamp))
		print "		Hash blocco predente: "+unicode(phash[indx])
		print "		Contenuto: "+unicode(vb[indx])
		print "Hash del blocco: "+unicode(block[indx])
	

main()
