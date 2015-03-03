import nxppy
from time import sleep

while 1:
	try:
		mifare = nxppy.Mifare()

		# Select the first available tag and return the UID
		uid = mifare.select()
		print uid

	except Exception:
		print('Erreur..')
	sleep(1)
