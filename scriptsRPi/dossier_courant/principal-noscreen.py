#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

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
from MySQLdb.constants import FIELD_TYPE

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
prix_boisson= 0.42 #TODO faire venir de la bd


########################################################################
### INITIALISATION
########################################################################

#Initialisation de l'écran LCD
#lcd.begin(16, 1)

my_conv = { FIELD_TYPE.FLOAT: float }

########################################################################
### FONCTIONS PERSONNELLES
########################################################################

#Ecriture parallele dans le terminal et dans le fichier de journal
#Usage : lprint(chaine) sans mettre de \n dans chaine ou apres : 
# le \n est inclus automatiquement dans l'ecriture dans les log
# et est inutile pour l'affichage dans un terminal avec print 
def lprint (chaine):
	print chaine
	#Ouverture initiale du fichier de journal
	f = open("loutre.log","a")    
	now = datetime.datetime.now().ctime()
	f.write( "[" + str(now) + "] : " + chaine + "\n")
	#Ouvrir et fermer le fichier a chaque fois permet une maj du fichier
	# m�me si le programme tourne
	f.close()


########################################################################
### BOUCLE PRINCIPALE
########################################################################

# Se connecter a la BD
db = MySQLdb.connect(host="localhost", user="python", passwd="jambeo", db="Loutre", conv=my_conv)


while 1:
	try:
		#Ouverture du lecteur NFC
		mifare=nxppy.Mifare()
		uid = mifare.select()
		lprint("Read UID : " + str(uid))
		
		##### Requete sur BD pour consulter le solde #####
		commande="SELECT Solde FROM Loutre.Personne WHERE ID='"
		commande+=str(uid)
		commande+="'"
		
		c = db.cursor()
		c.execute(commande)
		rows = c.fetchall() #rows va contenir tout les resultats
		c.close()
		# Traitement des resultats de notre requete
		for row in rows:
			solde=row[0]
		
		##### Fin de requete #####
		
				
		argentRestant = solde #Remplacer par le montant du backend
		#lcd.clear()
		#lcd.message("Argent restant : \n")
		lprint("Argent restant : ")
		#lcd.message(str(argentRestant) + unitePaiement)
		lprint(str(argentRestant) + unitePaiement)
		sleep(tempoLect1)
		
		instantLecture1=datetime.datetime.utcnow()
		
		a = True
		while a:
            #Apres expiration de la tempo la transaction est annulee
			now=datetime.datetime.now()
			if (now - instantLecture1) > datetime.timedelta(seconds = tempoLect2):
				break
			
			try:
				uid2 = mifare.select()
				lprint ("Read UID : " + str(uid2))

				if (uid2==uid):
					a = False
					
					##### Requete SQL pour le prelevement #####
					
					commande="UPDATE Personne SET Personne.Solde="
					commande+=str(solde-prix_boisson)
					commande+=" WHERE Personne.ID='"
					commande+=str(uid) + "'"

					#Test
					#lprint(commande)

					c = db.cursor()
					c.execute(commande)

					db.commit()
					##### Fin de requete #####
					
					#lcd.clear()
					#lcd.message("Moult"+unitePaiement+"\n")
					#lcd.message("ont ete prelevees.")
					lprint(str(prix_boisson)+unitePaiement+"ont ete prelevees")
					sleep(tempoPrelev)
					
			#Tant que on ne lit pas de carte, ne rien faire et recommencer
			except nxppy.SelectError:
				pass
	
	#Tant que on ne lit pas de carte, ne rien faire et recommencer
	except nxppy.SelectError:
		pass



