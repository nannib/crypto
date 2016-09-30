#!/usr/bin/python2
# RSA_NB_dkey.py
# Criptare e decriptare col cifrario RSA con input delle due chiavi Kpub e Kpriv
# programma ad uso didattico - only for didactic using
# il programma serve solo a capire i principi base dell RSA - the program intents only to explain the basic rules of RSA
# by Nanni Bassetti - http://www.nannibassetti.com - digitfor@gmail.com

def main():
	global e,d,n
	e = input('Inserisci e della chiave pubblica Kpub(e,n):')
	d = input('Inserisci d della chiave privata Kpriv(d,n):')
	n= input('Inserisci n:')
	print '-'*80
	print 'chiave pubblica KPub(',e,',',n,') chiave privata KPriv(',d,',',n,')'
	print '-'*80
	domanda=raw_input('Vuoi criptare o decriptare? (c/d):').lower()
	if domanda == 'c':
		criptare()
	if domanda == 'd':
		decriptare()
	
def criptare():
	global criptato,e,n
	testo = raw_input('Inserisci un testo da criptare:').lower()
	criptato=[pow(ord(char),e,n) for char in testo] 
		# la funzione pow(x,y,z) e' pari a x^y mod n, quindi criptato=(mess_chiaro^e) mod n
	print 'testo criptato: '
	char=str(criptato)
	char=char.replace(',','')
	char=char.replace('[','')
	criptato=char.replace(']','')
	print '', criptato

def decriptare():
	global decriptato,d,n
	testo = raw_input('Inserisci un testo da decriptare:').lower()
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