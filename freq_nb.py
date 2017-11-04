#!/usr/bin/python
# freq_nb.py
# Frequency Match Score calculator 
# programma ad uso didattico - only for didactic using
# by Nanni Bassetti - http://www.nannibassetti.com - digitfor@gmail.com


import collections
import textwrap

# frequenze delle lettere in italiano in ordine decrescente eaionlrtscdpumvghfbqz
mostfreqIT = 'eaionlrtscdpumvghfbqz'
#mostfreqENG='ETAOINSHRDLCUMWFGYPBVKJXQZ'

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
decriptato = ''
d=''
i=0
g = 0
j = 0
passo = 0
testo=''
# in input si da' la stringa formata dalle n-esime lettere del testo cifrato
# diviso per blocchi di x caratteri dove x e' la lunghezza della presunta chiave (kasiski)
# es. testo cifrato ktmcplor, x=4, ktmc plor, prima stringa: kp, seconda: tl, terza:mo, quarta:cr
# quindi alla variabile testo assegneremo prima kp, che sara' decriptata con chiave ogni singola 
# lettera dell'alfabeto, (quindi kp decriptata con a, poi kp con b, ecc.), poi la stringa uscente
# sara' analizzata ed ordinata per i caratteri con maggior frequenza ed infine si cerchera'
# il numero di caratteri che matchano con quelli presenti nell'alfabeto delle frequenze.
# per ogni corrispondenza trovata lo score aumenta di uno, le lettere che hanno score maggiore
# sono le candidate a comporre la chiave di decifrazione di Vigenere.
testo0 = raw_input('Inserisci la stringa da decriptare:').lower()
print 'testo:',testo0
kl = input('Inserisci lunghezza della chiave:')
print 'lunghezza:',kl
testo0=[testo0]

def gruppi():
	global testo
	for g in [g for text in testo0 for g in textwrap.wrap(text, kl)]: # divido il testo in gruppi di lunghezza kl
		print g
		if len(g)>=kl:
			testo+=g[j]
while j<kl:
	gruppi()
	print "N. Lett.  Decr.      OrdFreq.     Score"
	for c in alfabeto:	
		charc = alfabeto.index(c)
# decriptazione per ogni singola lettera alfabeto	 
		for t in testo:
			chart = alfabeto.index(t)
			newchar = chart - charc
			if newchar >= 26:
				newchar -= 26
			newchar = alfabeto[newchar]
			decriptato+=newchar
		cont=0
	# conta i caratteri piu' frequenti e li ordina, es. e (5 volte), z (2 volte), m (3 volte) 
	# ordinamento emz
		d=collections.Counter(decriptato)
		d=str(d)
		d=d.replace("Counter({'","")
		d=filter(lambda x: x.isalpha(), d) # filtra solo i caratteri
		d=d.replace("'","")
		d=d.replace(": ","")
		d=d.replace(", ","")
		d=d.replace("})","")
	# cicli for che confrontano quante lettere nella stringa coincidono col campione preso dall'alfabeto
	# delle frequenze ed incrementa il contatore di 1
		for car in d:
			for fc in mostfreqIT.lower()[:len(d)]:
				if car == fc :
					cont=cont+1		
		i=i+1
		print i,' ',c,'  ',decriptato,' ',d,' ',cont
		decriptato=''
	testo=''	
	j=j+1



