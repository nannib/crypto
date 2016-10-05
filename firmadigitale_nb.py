#!/usr/bin/python2
#!/usr/bin/python2
# firmadigitale_nb.py
# Simulatore di firma digitale
# programma ad uso didattico - only for didactic using
# il programma serve solo a capire i principi base dell RSA - the program intents only to explain the basic rules of RSA
# by Nanni Bassetti - http://www.nannibassetti.com - digitfor@gmail.com

import hashlib
def main():
	global e,d,n
	e = input('Inserisci e della chiave pubblica Kpub(e,n):')
	d = input('Inserisci d della chiave privata Kpriv(d,n):')
	n= input('Inserisci n:')
	print '-'*80
	print 'chiave pubblica KPub(',e,',',n,') chiave privata KPriv(',d,',',n,')'
	print '-'*80
	domanda=raw_input('Vuoi firmare o verificare? (f/v):').lower()
	if domanda == 'f':
		firmare()
	if domanda == 'v':
		verificare()
	
def firmare():
	global firma,d,n
	testo = raw_input('Inserisci un testo da firmare:').lower()
	hasht = hashlib.sha1(testo)
	hashtesto = hasht.hexdigest()
	firma=[pow(int(char,16),d,n) for char in hashtesto] 
		# la funzione pow(x,y,z) e' pari a x^y mod n, quindi criptato=(mess_chiaro^d) mod n
		# per la firma digitale si cripta con chiave privata
	print 'hash sha1 del testo:',hashtesto
	print " "
	print "*"*80
	char=str(firma)
	char=char.replace(',','')
	char=char.replace('[','')
	firma=char.replace(']','')
	print 'Firma: ',firma
	print "*"*80
	

def verificare():
	global decriptato,e,n
	firma = raw_input('Inserisci la firma da verificare:').lower()
	print " "
	print "-"*80
	print 'chiave pubblica KPub(',e,',',n,') chiave privata KPriv(',d,',',n,')'
	print "-"*80
	sp = []
	sp = firma.split(' ')
	decriptato = [pow(int(char),e,n) for char in sp] # decriptato = (firma^e) mod n si verifica usando la chiave pubblica
	decriptato=str(decriptato)
	decriptato=decriptato.replace(",","")
	decriptato=decriptato.replace("[","")
	decriptato=decriptato.replace("]","")
	decriptato=decriptato.replace("'","")
	sp = []
	sp = decriptato.split(' ')
	decriptato=[hex(int(char)) for char in sp]
	decriptato=str(decriptato)
	decriptato=decriptato.replace(",","")
	decriptato=decriptato.replace("[","")
	decriptato=decriptato.replace("]","")
	decriptato=decriptato.replace("'","")
	decriptato=decriptato.replace("0x","")
	decriptato=decriptato.replace(" ","")
	print 'hash del testo: ',decriptato  

main()