#!/usr/bin/env python
# -*- coding: utf-8 -*-

#LOUTRE
#Script principal
#Copyright : LOUTRE & Contributeurs, 2015.
#Licence GNU GPL v3

### VERSION PAS TESTEE SUR LE RPI ###

########################################################################
### IMPORT
########################################################################

import os
import datetime
from time import sleep

import nxppy
#from Adafruit_CharLCD import Adafruit_CharLCD

import MySQLdb


########################################################################
### CONSTANTES
########################################################################

#Temps d'attente lors de la lecture, en secondes
#(première lecture : affichage du solde, puis temporisation)
#(deuixème lecture : validation de la transaction)
#(si pas de deuxième lecture avant tempoLect2, annulation)
#tempoPrelev : temps de la tempo après validation de transaction
tempoLect1 = 1
tempoLect2 = 5
tempoPrelev = 1
unitePaiement=" groseilles "


########################################################################
### INITIALISATION
########################################################################

#Initialisation de l'écran LCD
#lcd.begin(16, 1)


########################################################################
### FONCTIONS PERSONNELLES
########################################################################

#Ecriture parallèle dans le terminal et dans le fichier de journal
#Usage : lprint(chaine) sans mettre de \n dans chaine ou après : 
# le \n est inclus automatiquement dans l'écriture dans les log
# et est inutile pour l'affichage dans un terminal avec print 
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

# Se connecter à la BD
db = MySQLdb.connect(host="localhost", user="python", passwd="jambeo", db="Loutre")



while 1:
	try:
		#Ouverture du lecteur NFC
		mifare=nxppy.Mifare()
		uid = mifare.select()
		lprint("Read UID : " + str(uid))
		
		##### Requete sur BD pour consulter le solde #####
		commande="SELECT Solde FROM Personne WHERE ID="
		commande+=str(uid)
		c = self.db.cursor()
		c.execute(commande)
		rows = c.fetchall() #rows va contenir tout les résultats
		c.close()
		# Traitement des résultats de notre requête
		solde=row[0]
		for row in rows:
			solde=row[0]
		##### Fin de requete #####
		
				
		argentRestant = solde #Remplacer par le montant du backend
		lcd.clear()
		lcd.message("Argent restant : \n")
		lprint("Argent restant : ")
		lcd.message(str(argentRestant) + unitePaiement)
		lprint(str(argentRestant) + unitePaiement)
		sleep(tempoLect1)
		
		instantLecture1=datetime.datetime.utcnow()
		
		a = True
		while a:
            #Après expiration de la tempo la transaction est annulée
			now=datetime.datetime.now()
			if (now - instantLecture1) > datetime.timedelta(seconds = tempoLect2):
				break
			
			try:
				uid2 = mifare.select()
				lprint ("Read UID : " + str(uid2))

				if (uid2==uid):
					a = False
					
					##### Requete SQL pour le prélèvement #####
					commande="INSERT INTO (ID_Etudiant,Montant) VALUES ("
					commande+=str(uid)
					commande+=", SELECT - prix_boisson FROM parametres"
					c = self.db.cursor()
					c.execute(commande)
					##### Fin de requete #####
					
					lcd.clear()
					lcd.message("Moult"+unitePaiement+"\n")
					lcd.message("ont été prélevées.")
					lprint("Moult"+unitePaiement+"ont été prélevées")
					sleep(tempoPrelev)
					
			#Tant que on ne lit pas de carte, ne rien faire et recommencer
			except nxppy.SelectError:
				pass
	
	#Tant que on ne lit pas de carte, ne rien faire et recommencer
	except nxppy.SelectError:
		pass



