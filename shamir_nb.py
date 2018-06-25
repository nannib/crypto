# Shamir_nb.py
# Shamir's Secret Sharing Scheme
# programma ad uso didattico - only for didactic using
# by Nanni Bassetti - http://www.nannibassetti.com - digitfor@gmail.com

import random, math
def main():

	global s,n,k,s0
	s = int(input('Inserisci chiave segreta numerica (secret):'))
	print 'chiave:',s
	n = int(input('Inserisci numero di partecipanti (share):'))
	print 'partecipanti:',n
	k = int(input('Inserisci numero minimo di pezzi per ricostruire la chiave, deve essere <= della chiave (Threshold):'))
	print 'Soglia:',k
	if k>n:
		print "la soglia deve essere minore o uguale al numero dei partecipanti!"
		print "nuova soglia:",n
		k=n
	print "Soglia:",k,"Partecipanti:",n
# valorizzazione variabili	
	p=1000763 # numero primo >n
	s0=s
	#s0=1234
	#k=3
	#n=6
	ss=range(0,n)
	prod=range(0,n+1)
	for i in range(0,n+1):
		prod[i]=1
	x=range(0,n+1)
	r=range(0,p-1)
	s=range(0,n)
	pol=range(0,n+1)
	pindx=range(0,k)
	pezzi=range(0,k)
	secret=0
	for i in range(0,n):
		x[i]=i+1
		pol[i]=0
# scelta casuale dei coefficenti		
	for i in range (0,k-1):
		r[i]=random.randint(0,p)
# calcolo dei polinomi		
	for i in range (0,n):
		for j in range (0,k-1):
			pol[i]+=r[j]*(x[i]**(j+1))
			
# somma del segreto al polinomio: es: r0*x0^2 + r1*x0^1 + s0
	for j in range (0,n):
		s[j]=(s0+pol[j]) % p
		
# stampa dei pezzi ricavati	
	for i in range(0,n):
		print "pezzo(",i,") ",s[i]

	print "\n\nInserisci gli indici dei ",k," pezzi che vuoi usare per la ricostruzione, separati dalla virgola (es. 0,2,3):"
	pz=input("pezzi:")
	print 'valori dei pezzi:'
	kk=-1
	for i in pz:
		print s[i],
		kk=kk+1
		pindx[kk]=i
		pezzi[kk]=s[i]
	
# pindx contiene il numero d'indice del vettore s
# pezzi sono i pezzi che vogliamo usare per ricostruire il segreto	

	j=0
# creazione della produttoria (0-xj)/(xi-xj) con j<>i
	for i in range(0,k):
		t=i
		for j in range(1,k):
			if j==i or j>(k-1):
				j=0
			if t>0:
				t=i-1
			
			prod[i]=(prod[i]*(((0-x[pindx[j]])/float(x[pindx[i]]-x[pindx[j]]))))
			
		
# prodotto del valore del pezzo per il prodotto relativo
		ss[i]=int(pezzi[i]*prod[i])
		
# sommatoria di tutti i prodotti pezzo*produttoria
	for i in range(0,k):
		secret+=ss[i] 
# operazione segreto modulo p (il numero primo impostato inizialmente)
	secret=(secret) % p
	
	
	print "\nCHIAVE:",secret

main()