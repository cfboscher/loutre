#!/usr/bin/env python
# -*- coding: latin-1 -*-

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

#import nxppy
#from Adafruit_CharLCD import Adafruit_CharLCD


########################################################################
### CONSTANTES
########################################################################

#Prix d'une consommation
prixUnitaire = 42

#Temps d'attente lors de la lecture, en secondes
#(première lecture : affichage du solde, puis temporisation)
#(deuixème lecture : validation de la transaction)
#(si pas de deuxième lecture avant tempoLect2, annulation)
tempoLect1 = 1
tempoLect2 = 5
unitePaiement=" groseilles "


########################################################################
### INITIALISATION
########################################################################

#Initialisation de l'écran LCD
#lcd.begin(16, 1)

#Ouverture du lecteur NFC
mifare=nxppy.Mifare()


########################################################################
### FONCTIONS PERSONNELLES
########################################################################

#Ecriture parallèle dans le terminal et dans le fichier de journal
def lprint (chaine):
	print chaine
	#Ouverture initiale du fichier de journal
	f = open("loutre.log","a")    
	now = datetime.datetime.now().ctime()
	f.write( "[" + str(now) + "] : " + chaine + "\n")
	#Ouvrir et fermer le fichier à chaque fois permet une màj du fichier
	# même si le programme tourne
	f.close()


########################################################################
### BOUCLE PRINCIPALE
########################################################################

while 1:
	try:
		uid = mifare.select()
		lprint("Read UID : " + str(uid))
		### Insérer appel procédure mySQL pour l'affichage ###
		argentRestant = 500 #Remplacer par le montant de la fin de dos
		#lcd.clear()
		#lcd.message("Argent restant : \n")
		lprint("Argent restant : \n")
		#lcd.message(str(argentRestant) + nomMonnaieyes)
		lprint(str(argentRestant) + nomMonnaie)
		sleep(tempoLect1)
		
		instantLecture1=datetime.datetime.utcnow()
		
		a = True
		while a:
			#Après expiration de la tempo la transaction est annulée
			now=datetime.datetime.now()
			if (now - instantLecture1) > timedelta(seconds = tempoLect2):
				break
			
			try:
				uid2 = mifare.select()
				lprint ("Read UID : " + str(uid2))

				if (uid2==uid):
					a = false
					### Insérer appel procédure MySQL (mon langage de requete structuré )  pour le prélèvement ###
					#lcd.clear()
					#lcd.message(str(prixUnitaire)+unitePaiement+"\n")
					#lcd.message("ont été prélevées.")
					lprint(str(prixUnitaire)+unitePaiement+"ont été prélevées")
					
			#Tant que on ne lit pas de carte, ne rien faire et recommencer
			except nxppy.SelectError:
				pass

	#Tant que on ne lit pas de carte, ne rien faire et recommencer
	except nxppy.SelectError:
		pass


