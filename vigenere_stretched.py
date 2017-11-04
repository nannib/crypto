#!/usr/bin/python
# VIGENERE_stretched.py
# Criptare e decriptare col cifrario di Vigenere col key stretching
# il programma serve solo a capire i principi base dell key stretching - the program intents only to explain the basic rules of key stretching
# by Nanni Bassetti - http://www.nannibassetti.com - digitfor@gmail.com

import hashlib
encoded=""
alfabeto = 'abcdefghijklmnopqrstuvwxyz0123456789'
criptato=''
decriptato=''
i=0

def main():
	domanda=raw_input('Vuoi criptare o decriptare? (c/d):').lower()
	if domanda == 'c':
		criptare()
	if domanda == 'd':
		decriptare()

def criptare():
	global criptato,i
	testo = raw_input('Inserisci un testo da criptare:').lower()
	print 'testo:',testo

	pw = raw_input('Inserisci una password di criptazione:').lower()
	print 'Password:',pw
	while i<500000:
		i=i+1
		hash_pw_salt = hashlib.sha256(pw+unicode(i))
		chiave = hash_pw_salt.hexdigest()
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
		if newchar >= 36:
			newchar -= 36
		newchar = alfabeto[newchar]
		criptato+=newchar
	print 'testo criptato: ',criptato 

def decriptare():
	global decriptato,i
	testo = raw_input('Inserisci un testo da decriptare:').lower()
	print 'testo:',testo

	pw = raw_input('Inserisci una password di decriptazione:').lower()
	print 'password:',pw
	while i<500000:
		i=i+1
		hash_pw_salt = hashlib.sha256(pw+unicode(i))
		chiave = hash_pw_salt.hexdigest()
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
		if newchar >= 36:
			newchar -= 36
		newchar = alfabeto[newchar]
		decriptato+=newchar
	print 'testo decriptato: ',decriptato  

main()
