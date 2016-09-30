#!/usr/bin/python2
# VIGENERE_NB.py
# Criptare e decriptare col cifrario di Vigenere
# programma ad uso didattico - only for didactic using
# by Nanni Bassetti - http://www.nannibassetti.com - digitfor@gmail.com

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
criptato=''
decriptato=''

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

	chiave = raw_input('Inserisci un chiave di criptazione:').lower()
	print 'chiave:',chiave

	while len(chiave)<len(testo):
        #controllo se la chiave e' piu' corta del testi
		chiave+=chiave
        #This repeats the chiave.
		if len(chiave)>len(testo):
            #controllo se la chiave e' piu' lunga del testo
			newkey=chiave[:len(testo)]
			print 'newkey=',newkey 
            #qui si taglia la chiave alla lunghezza del testo
	for t,c in zip(testo,chiave):
		chart = alfabeto.index(t)
		charc = alfabeto.index(c)
		newchar = chart + charc
		if newchar >= 26:
			newchar -= 26
		newchar = alfabeto[newchar]
		criptato+=newchar
	print 'testo criptato: ',criptato 

def decriptare():
	global decriptato
	testo = raw_input('Inserisci un testo da decriptare:').lower()
	print 'testo:',testo

	chiave = raw_input('Inserisci un chiave di decriptazione:').lower()
	print 'chiave:',chiave

	while len(chiave)<len(testo):
        #controllo se la chiave e' piu' corta del testi
			chiave+=chiave
        #This repeats the chiave.
        if len(chiave)>len(testo):
            #controllo se la chiave e' piu' lunga del testo
            newkey=chiave[:len(testo)]
            #qui si taglia la chiave quando finisce il testo
	for t,c in zip(testo,chiave):
		chart = alfabeto.index(t)
		charc = alfabeto.index(c)
		newchar = chart - charc
		if newchar >= 26:
			newchar -= 26
		newchar = alfabeto[newchar]
		decriptato+=newchar
	print 'testo decriptato: ',decriptato  

main()