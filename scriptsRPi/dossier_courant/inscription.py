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

import RPi.GPIO as GPIO

import getpass

########################################################################
### CONSTANTES
########################################################################

soldeDepart=5.0

########################################################################
### INITIALISATION
########################################################################

#Initialisation de l'écran LCD
lcd = Adafruit_CharLCD()
lcd.begin(16, 1)

#Init led
ledPin=13
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

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


#Fonction pour 
def entrerMdP():

    pprompt = lambda: (getpass.getpass('Mot de passe : '), getpass.getpass('Confirmation mot de passe : '))

    p1, p2 = pprompt()
    while p1 != p2:
        print('/!\\ Mots de passe différents /!\\')
        p1, p2 = pprompt()

    return p1


########################################################################
### BOUCLE PRINCIPALE
########################################################################

# Se connecter a la BD
db = MySQLdb.connect(host="localhost", user="python", passwd="jambeo", db="Loutre")


while 1:
	try:
		lcd.clear()
		lcd.message(" Inscription a\n     LOUTRE")
		GPIO.output(ledPin, GPIO.HIGH)
		sleep(0.5)
		GPIO.output(ledPin, GPIO.LOW)
		sleep(0.5)
		#Ouverture du lecteur NFC
		mifare=nxppy.Mifare()
		uid = mifare.select()
		lprint("Lecture UID pour inscription : " + str(uid))
		
		lcd.clear()
		lcd.message("Nouvel util :\n"+str(uid))

		#Entr�ee clavier des infos du nouvel utilisateur
		GPIO.output(ledPin, GPIO.HIGH)
		print("Veuillez rentrez les informations demandées : ")
		nom = raw_input("Nom : ")
		prenom = raw_input("Prénom : ")
		login = raw_input("Sobriquet : ")
	        #password = raw_input("Mot de passe : ")#TODO hasher le pass en md5
		password = entrerMdP();

		##### Requete sur BD pour inscrire l'utilisateur #####
		#ID Nom Prenom Role(1) Solde Password
		commande="INSERT INTO Personne(ID,Login,Nom,Prenom,Role,Solde,Password) VALUES ("
		commande+="'"+str(uid)+"','"+str(login)+"','"+str(nom)+"','"+str(prenom)+"',"+str(1)+","+str(soldeDepart)+",'"+str(password)+"')"

	        #Test
		#lprint(commande)

		c = db.cursor()
		c.execute(commande)

		db.commit()
		##### Fin de requete #####

		lprint("Nouvel utilisateur : " + nom + " " + prenom + "\n")

		lcd.clear()
		lcd.message("  Bravo !\nInscr reussie")
		
		cmptr=0
		while(cmptr<10):
			cmptr+=1
			GPIO.output(ledPin, GPIO.HIGH)
			sleep(0.3)
			GPIO.output(ledPin, GPIO.LOW)
			sleep(0.3)
											
	#Tant que on ne lit pas de carte, ne rien faire et recommencer
	except nxppy.SelectError:
		pass



