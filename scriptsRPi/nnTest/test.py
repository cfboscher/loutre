#!/usr/bin/env python
# -*- coding: latin-1 -*-

#Test d'écriture de log
#En fermant et réouvrant le fichier à chaque itération, on peut lire le
# fichier log pendant que le script tourne.
#Le fichier n'est écrit vraiment que quand on le .close()

from time import sleep
import datetime

#Ecriture parallèle dans le terminal et dans le fichier de log
def lprint (chaine):
	print chaine
	#Ouverture initiale du fichier de log
	f = open("loutre.log","a")    
	now = datetime.datetime.now().ctime()
	f.write( "[" + str(now) + "] : " + chaine + "\n")
	#Ouvrir et fermer le fichier à chaque fois permet une màj du fichier
	# même si le programme tourne
	f.close()


lprint("Coucou les amis")
