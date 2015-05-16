#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

#LOUTRE
#Script d'inscription
#Copyright : LOUTRE & Contributeurs, 2015.
#Licence GNU GPL v3

########################################################################
### IMPORT
########################################################################

import os

import datetime

from time import sleep

import nxppy
from Adafruit_CharLCD import Adafruit_CharLCD

import MySQLdb

########################################################################
### CONSTANTES
########################################################################

soldeDepart=5.0

########################################################################
### INITIALISATION
########################################################################

#Initialisation de l'Ã©cran LCD
lcd = Adafruit_CharLCD()
lcd.begin(16, 1)

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
	# même si le programme tourne
	f.close()


########################################################################
### BOUCLE PRINCIPALE
########################################################################

# Se connecter a la BD
db = MySQLdb.connect(host="localhost", user="python", passwd="jambeo", db="Loutre")


while 1:
	try:
		lcd.clear()
		lcd.message(" Inscription a\n     LOUTRE")
		sleep(0.1)
		#Ouverture du lecteur NFC
		mifare=nxppy.Mifare()
		uid = mifare.select()
		lprint("Lecture UID pour inscription : " + str(uid))
		
		lcd.clear()
		lcd.message("Nouvel util :\n"+str(uid))

		#EntrÃee clavier es infos du nouvel utilisateur
		print("Veuillez rentrez les informations demandÃ©s : ")
		nom = raw_input("Nom : ")
		prenom = raw_input("PrÃ©nom : ")
	        password = raw_input("Mot de passe : ")#TODO hasher le pass en md5

		##### Requete sur BD pour inscrire l'utilisateur #####
		#ID Nom Prenom Role(1) Solde Password
		commande="INSERT INTO Personne(ID,Nom,Prenom,Role,Solde,Password) VALUES ("
		commande+="'"+str(uid)+"','"+str(nom)+"','"+str(prenom)+"',"+str(1)+","+str(soldeDepart)+",'"+str(password)+"')"

	        #Test
		#lprint(commande)

		c = db.cursor()
		c.execute(commande)

		db.commit()
		##### Fin de requete #####

		lprint("Nouvel utilisateur : " + nom + " " + prenom)

		lcd.clear()
		lcd.message("  Bravo !\nInscr reussie")
		sleep(5)
									
	#Tant que on ne lit pas de carte, ne rien faire et recommencer
	except nxppy.SelectError:
		pass



