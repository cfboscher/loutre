#!/usr/bin/env python
# -*- coding: utf-8 -*-

#LOUTRE
#Script principal
#Copyright : LOUTRE & Contributeurs, 2015.
#Licence GNU GPL v3

### VERSION DE TEST SANS GESTION DE L'ECRAN LCD ###

########################################################################
### IMPORT
########################################################################

import os
import datetime
from time import sleep

import nxppy
#from Adafruit_CharLCD import Adafruit_CharLCD


########################################################################
### CONSTANTES
########################################################################

#Prix d'une consommation
prixUnitaire = 42

#Temps d'attente lors de la lecture, en secondes
#(premiÃ¨re lecture : affichage du solde, puis temporisation)
#(deuixÃ¨me lecture : validation de la transaction)
#(si pas de deuxiÃ¨me lecture avant tempoLect2, annulation)
tempoLect1 = 1
tempoLect2 = 5
unitePaiement=" groseilles "


########################################################################
### INITIALISATION
########################################################################

#Initialisation de l'Ã©cran LCD
#lcd.begin(16, 1)


########################################################################
### FONCTIONS PERSONNELLES
########################################################################

#Ecriture parallÃ¨le dans le terminal et dans le fichier de journal
def lprint (chaine):
	print chaine
	#Ouverture initiale du fichier de journal
	f = open("loutre.log","a")    
	now = datetime.datetime.now().ctime()
	f.write( "[" + str(now) + "] : " + chaine + "\n")
	#Ouvrir et fermer le fichier Ã  chaque fois permet une mÃ j du fichier
	# mÃªme si le programme tourne
	f.close()


########################################################################
### BOUCLE PRINCIPALE
########################################################################

while 1:
	try:
		#Ouverture du lecteur NFC
		mifare=nxppy.Mifare()
		uid = mifare.select()
		print "Lecture 1"
		print uid
		lprint("Read UID : " + str(uid))
		### InsÃ©rer appel procÃ©dure mySQL pour l'affichage ###
		argentRestant = 500 #Remplacer par le montant de la fin de dos
		#lcd.clear()
		#lcd.message("Argent restant : \n")
		lprint("Argent restant : \n")
		#lcd.message(str(argentRestant) + nomMonnaieyes)
		lprint(str(argentRestant) + unitePaiement)
		sleep(tempoLect1)
		
		instantLecture1=datetime.datetime.utcnow()
		
		a = True
		while a:
			print "Boucle 2"
                        #AprÃ¨s expiration de la tempo la transaction est annulÃe
			now=datetime.datetime.now()
			if (now - instantLecture1) > datetime.timedelta(seconds = tempoLect2):
				break
			
			try:
				uid2 = mifare.select()
				lprint ("Read UID : " + str(uid2))

				if (uid2==uid):
					a = False
					### InsÃ©rer appel procÃ©dure MySQL (mon langage de requete structurÃ© )  pour le prÃ©lÃ¨vement ###
					#lcd.clear()
					#lcd.message(str(prixUnitaire)+unitePaiement+"\n")
					#lcd.message("ont Ã©tÃ© prÃ©levÃ©es.")
					lprint(str(prixUnitaire)+unitePaiement+"ont Ã©tÃ© prÃ©levÃ©es")
					
			#Tant que on ne lit pas de carte, ne rien faire et recommencer
			except nxppy.SelectError:
				pass

	#Tant que on ne lit pas de carte, ne rien faire et recommencer
	except nxppy.SelectError:
		pass
	        print "except 1"
		sleep(1)



