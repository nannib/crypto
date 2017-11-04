#!/usr/bin/python
# RSA_NB.py
# Criptare e decriptare col cifrario RSA 
# programma ad uso didattico - only for didactic using
# il programma serve solo a capire i principi base dell RSA - the program intents only to explain the basic rules of RSA
# by Nanni Bassetti - http://www.nannibassetti.com - digitfor@gmail.com


def main():
	domanda=raw_input('Vuoi criptare o decriptare? (c/d):').lower()
	if domanda == 'c':
		criptare()
	if domanda == 'd':
		decriptare()

def criptare():
	global criptato
	testo = raw_input('Inserisci un testo da criptare:').lower()
	print 'testo:',testo

	p = input('Inserisci numero primo P > 1 (meglio se >10):')
	print 'p:',p
	q = input('Inserisci numero primo Q > 1 (meglio se >10):')
	print 'q:',q
	n = p * q   # calcolo il modulo n
	z = (p-1)*(q-1) # calcolo la funzione di Eulero
	r1=0
	i=0
	e=0
	# trovo l'esponente pubblico e che NON ha fattori comuni con z, quindi  z mod e > 0
	# tale che sia primo con (p-1)(q-1) quindi non deve avere fattori primi in comune
	#e deve essere dispari, dato che (p-1)(q-1) non puo' essere primo poiche' e' pari.
	while r1 == 0 :
		i = i+1
		r1 = z % i
		e = i
	print 'Esponente pubblico e:',e
	for d in range(3, z, 2): 
	# cerco l'esponente privato d, tale che (d*e)-1 sia divisibile per z
	# la funzione range parte da 3 e aggiunge 2 unita' (esculde i num pari) fino a raggiungere il numero z ma non includendolo.
	# pari * dispari = pari ma pari<>quoziente*pari+1 e quindi il resto non puo' mai essere 1,perche' la divisione deve dare resto 0, pertanto d deve essere dispari.
		if d * e % z == 1:
			break
	else:
		raise AssertionError("non riesco a trovare 'd'")


	print 'Esponente privato d:',d 
	print 'modulo n: ',n, ' Eulero (p-1)(q-1): ',z
	print '-'*80
	print 'chiave pubblica KPub(',e,',',n,') chiave privata KPriv(',d,',',n,')'
	criptato=[pow(ord(char),e,n) for char in testo] 
		# la funzione pow(x,y,z) e' pari a x^y mod n, quindi criptato=(mess_chiaro^e) mod n
	print 'testo criptato: '
	char=str(criptato)
	char=char.replace(',','')
	char=char.replace('[','')
	criptato=char.replace(']','')
	print '', criptato

def decriptare():
	global decriptato
	testo = raw_input('Inserisci un testo da decriptare:').lower()
	print 'testo criptato (i numeri separati dallo spazio, es: 52 34,ecc.):',testo

	p = input('Inserisci numero primo P > 1 (meglio se >10):')
	print 'p:',p
	q = input('Inserisci numero primo Q > 1 (meglio se >10):')
	print 'q:',q
	n = p * q
	z = (p-1)*(q-1)
	r1=0
	i=0
	e=0
	# trovo l'esponente pubblico e che NON ha fattori comuni con z, quindi  z mod e > 0
	# tale che sia primo con (p-1)(q-1) quindi non deve avere fattori primi in comune
	#e deve essere dispari, dato che (p-1)(q-1) non puo' essere primo poiche' e' pari.
	while r1 == 0 :
		i = i+1
		r1 = z % i
		e = i
	print 'Esponente pubblico e:',e

	for d in range(3, z, 2): 
	# cerco l'esponente privato d, tale che (d*e)-1 sia divisibile per z
	# la funzione range parte da 3 e aggiunge 2 unita' (esculde i num pari) fino a raggiungere il numero z ma non includendolo
	# pari * dispari = pari ma pari<>quoziente*pari+1 e quindi il resto non puo' mai essere 1 pertanto d deve essere dispari
		if d * e % z == 1:
			break
	else:
		raise AssertionError("non riesco a trovare 'd'")


	print 'Esponente privato d:',d 
	print 'modulo n: ',n, ' Eulero(p-1)(q-1): ',z
	print '-'*80
	print 'chiave pubblica KPub(',e,',',n,') chiave privata KPriv(',d,',',n,')'
	sp = []
	sp = testo.split(' ')
	decriptato = [chr(pow(int(char),d,n)) for char in sp] # decriptato = (mess_crypt^d) mod n
	char=str(decriptato)
	char=char.replace(", ","")
	char=char.replace("[","")
	char=char.replace("]","")
	decriptato=char.replace("'","")
	print 'testo decriptato: ',decriptato  

main()
