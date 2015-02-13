#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep

lcd = Adafruit_CharLCD()

lcd.begin(16, 1)

ligne1='Ah oui oui'
ligne2='je vois le truc'
i=0

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

while 1:
    lcd.clear()
    lcd.message(ligne1+str(i)+'\n') 
    print(ligne1+str(i)+'\n')
    lcd.message(ligne2+str(i)) 
    print(ligne2+str(i))
    i=i+1
    sleep(2)


